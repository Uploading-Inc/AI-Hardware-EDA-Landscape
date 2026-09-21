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
MARKDOWN_LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
REFERENCE_DEFINITION_PATTERN = re.compile(
    r"^\s{0,3}\[(?!\^)([^\]]+)\]:\s*(.+)$", re.MULTILINE
)
HTML_TARGET_PATTERN = re.compile(r"\b(?:src|href)=[\"']([^\"']+)[\"']", re.IGNORECASE)
FENCE_PATTERN = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")

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

    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        marker = FENCE_PATTERN.match(line)
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
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
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


def validate_markdown(errors: list[str]) -> tuple[int, int]:
    markdown_files = repository_files("*.md")
    checked_links = 0

    for path in markdown_files:
        prose = prose_outside_fences(path, errors)
        link_matches = list(MARKDOWN_LINK_PATTERN.finditer(prose))
        reference_matches = list(REFERENCE_DEFINITION_PATTERN.finditer(prose))
        html_matches = list(HTML_TARGET_PATTERN.finditer(prose))
        raw_targets = [match.group(1) for match in [*link_matches, *html_matches]]
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
            for line in path.read_text(encoding="utf-8").splitlines()
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
