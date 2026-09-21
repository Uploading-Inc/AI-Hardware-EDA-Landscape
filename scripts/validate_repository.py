#!/usr/bin/env python3
"""Validate local documentation links, research-card structure, and SVG assets."""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
IGNORED_PARTS = {".git", "_coordination"}
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FENCE_PATTERN = re.compile(r"^\s*(```|~~~)")

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
    open_fence: str | None = None

    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        marker = FENCE_PATTERN.match(line)
        if marker:
            token = marker.group(1)
            if open_fence is None:
                open_fence = token
            elif open_fence == token:
                open_fence = None
            continue
        if open_fence is None:
            prose.append(line)

    if open_fence is not None:
        errors.append(f"{path.relative_to(ROOT)}: unclosed {open_fence} code fence")

    return "\n".join(prose)


def local_link_target(raw_target: str) -> str | None:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]

    parsed = urlparse(target)
    if parsed.scheme or target.startswith(("#", "//")):
        return None

    path_only = unquote(target.split("#", 1)[0])
    return path_only or None


def validate_markdown(errors: list[str]) -> tuple[int, int]:
    markdown_files = repository_files("*.md")
    checked_links = 0

    for path in markdown_files:
        prose = prose_outside_fences(path, errors)
        for match in LINK_PATTERN.finditer(prose):
            target = local_link_target(match.group(1))
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
