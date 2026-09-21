#!/usr/bin/env python3
"""Validate local documentation links, research-card structure, and SVG assets."""

from __future__ import annotations

import re
import shlex
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
IGNORED_PARTS = {".git", "_coordination"}
REFERENCE_DEFINITION_PATTERN = re.compile(
    r"^\s{0,3}\[(?!\^)([^\]]+)\]:\s*(.+)$", re.MULTILINE
)
HTML_TARGET_PATTERN = re.compile(r"\b(?:src|href)=[\"']([^\"']+)[\"']", re.IGNORECASE)
FENCE_PATTERN = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")

REQUIRED_CARD_HEADINGS = {
    "## One-sentence definition",
    "## Why it exists",
    "## Benchmark anatomy",
    "## Evaluation pipeline",
    "## What it demonstrates",
    "## What it does not demonstrate",
    "## Reproducibility",
    "## Open questions",
}


def repository_files(pattern: str) -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob(pattern)
        if not IGNORED_PARTS.intersection(path.relative_to(ROOT).parts)
    )


def prose_outside_fences(path: Path, errors: list[str]) -> str:
    prose: list[str] = []
    open_fence: tuple[str, int] | None = None

    for line in path.read_text(encoding="utf-8").splitlines():
        marker = FENCE_PATTERN.match(line)
        if (
            marker
            and open_fence is None
            and marker.group(1).startswith("`")
            and "`" in marker.group(2)
        ):
            marker = None
        if marker:
            token = marker.group(1)
            if open_fence is None:
                open_fence = (token[0], len(token))
            elif (
                token[0] == open_fence[0]
                and len(token) >= open_fence[1]
                and not marker.group(2).strip()
            ):
                open_fence = None
            continue
        if open_fence is None:
            prose.append(line)

    if open_fence is not None:
        marker = open_fence[0] * open_fence[1]
        errors.append(f"{path.relative_to(ROOT)}: unclosed {marker} code fence")

    return "\n".join(prose)


def local_link_target(raw_target: str) -> str | None:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        try:
            parts = shlex.split(target)
        except ValueError:
            parts = [target]
        if parts:
            target = parts[0]

    parsed = urlparse(target)
    if parsed.scheme or target.startswith(("#", "//")):
        return None

    path_only = unquote(parsed.path)
    return path_only or None


def prose_without_inline_code(prose: str) -> str:
    """Remove inline code spans while preserving line breaks and offsets."""
    output = list(prose)
    index = 0
    while index < len(prose):
        if prose[index] != "`" or is_escaped(prose, index):
            index += 1
            continue

        run_end = index
        while run_end < len(prose) and prose[run_end] == "`":
            run_end += 1
        delimiter = prose[index:run_end]
        close = prose.find(delimiter, run_end)
        while close != -1 and (
            (close > 0 and prose[close - 1] == "`")
            or (close + len(delimiter) < len(prose) and prose[close + len(delimiter)] == "`")
        ):
            close = prose.find(delimiter, close + len(delimiter))
        if close == -1:
            index = run_end
            continue

        for position in range(index, close + len(delimiter)):
            if output[position] != "\n":
                output[position] = " "
        index = close + len(delimiter)

    return "".join(output)


def is_escaped(text: str, index: int) -> bool:
    backslashes = 0
    cursor = index - 1
    while cursor >= 0 and text[cursor] == "\\":
        backslashes += 1
        cursor -= 1
    return backslashes % 2 == 1


def markdown_inline_targets(prose: str) -> list[str]:
    """Extract inline link destinations with balanced-parenthesis support."""
    targets: list[str] = []
    label_stack: list[int] = []
    index = 0
    while index < len(prose):
        character = prose[index]
        if character == "[" and not is_escaped(prose, index):
            label_stack.append(index)
        elif character == "]" and not is_escaped(prose, index) and label_stack:
            label_stack.pop()
            if index + 1 < len(prose) and prose[index + 1] == "(":
                cursor = index + 2
                depth = 1
                escaped = False
                while cursor < len(prose):
                    target_character = prose[cursor]
                    if escaped:
                        escaped = False
                    elif target_character == "\\":
                        escaped = True
                    elif target_character == "(":
                        depth += 1
                    elif target_character == ")":
                        depth -= 1
                        if depth == 0:
                            targets.append(prose[index + 2 : cursor])
                            break
                    cursor += 1
        index += 1
    return targets


def validate_markdown(errors: list[str]) -> tuple[int, int]:
    markdown_files = repository_files("*.md")
    checked_links = 0

    for path in markdown_files:
        prose = prose_without_inline_code(prose_outside_fences(path, errors))
        reference_matches = list(REFERENCE_DEFINITION_PATTERN.finditer(prose))
        html_matches = list(HTML_TARGET_PATTERN.finditer(prose))
        raw_targets = markdown_inline_targets(prose)
        raw_targets.extend(match.group(1) for match in html_matches)
        raw_targets.extend(match.group(2) for match in reference_matches)
        for raw_target in raw_targets:
            target = local_link_target(raw_target)
            if target is None:
                continue
            checked_links += 1
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(
                    f"{path.relative_to(ROOT)}: missing local link target {target!r}"
                )

    return len(markdown_files), checked_links


def validate_benchmark_cards(errors: list[str]) -> int:
    cards = sorted((ROOT / "research" / "benchmarks").glob("*.md"))
    for path in cards:
        headings = {
            line.strip()
            for line in prose_outside_fences(path, []).splitlines()
            if line.startswith("## ")
        }
        missing = sorted(REQUIRED_CARD_HEADINGS - headings)
        if missing:
            errors.append(
                f"{path.relative_to(ROOT)}: missing required headings: {', '.join(missing)}"
            )
    return len(cards)


def validate_svg_assets(errors: list[str]) -> int:
    assets = repository_files("*.svg")
    for path in assets:
        try:
            ET.parse(path)
        except ET.ParseError as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid SVG/XML: {exc}")
    return len(assets)


def main() -> int:
    errors: list[str] = []
    markdown_count, link_count = validate_markdown(errors)
    card_count = validate_benchmark_cards(errors)
    svg_count = validate_svg_assets(errors)

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Repository validation passed: "
        f"{markdown_count} Markdown files, {link_count} local links, "
        f"{card_count} benchmark cards, {svg_count} SVG assets"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
