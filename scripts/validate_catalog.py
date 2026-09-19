#!/usr/bin/env python3
"""Validate the seed benchmark catalog using only the Python standard library."""

from __future__ import annotations

import csv
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "benchmarks.csv"

REQUIRED = {
    "id",
    "name",
    "year",
    "domain",
    "task",
    "interaction",
    "oracle",
    "repo_context",
    "paper_url",
    "code_url",
    "status",
    "notes",
}
INTERACTIONS = {"single-shot", "iterative", "tool-using", "long-horizon-agent"}
STATUSES = {"seed", "verified", "needs-review"}
BOOLEANS = {"true", "false"}


def valid_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def main() -> int:
    errors: list[str] = []
    seen: set[str] = set()

    with CATALOG.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fields = set(reader.fieldnames or [])
        if fields != REQUIRED:
            errors.append(
                f"header mismatch: missing={sorted(REQUIRED - fields)}, "
                f"unexpected={sorted(fields - REQUIRED)}"
            )

        rows = list(reader)

    for line, row in enumerate(rows, start=2):
        prefix = f"line {line} ({row.get('id') or 'missing-id'})"
        missing = sorted(field for field in REQUIRED if not row.get(field, "").strip() and field != "code_url")
        if missing:
            errors.append(f"{prefix}: empty required fields: {', '.join(missing)}")

        item_id = row.get("id", "")
        if item_id in seen:
            errors.append(f"{prefix}: duplicate id")
        seen.add(item_id)

        try:
            year = int(row.get("year", ""))
            if not 2020 <= year <= 2100:
                errors.append(f"{prefix}: implausible year {year}")
        except ValueError:
            errors.append(f"{prefix}: year is not an integer")

        if row.get("interaction") not in INTERACTIONS:
            errors.append(f"{prefix}: invalid interaction {row.get('interaction')!r}")
        if row.get("status") not in STATUSES:
            errors.append(f"{prefix}: invalid status {row.get('status')!r}")
        if row.get("repo_context") not in BOOLEANS:
            errors.append(f"{prefix}: repo_context must be true or false")

        for field in ("paper_url", "code_url"):
            value = row.get(field, "").strip()
            if value and not valid_url(value):
                errors.append(f"{prefix}: invalid {field}: {value}")

    if errors:
        print("Catalog validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Catalog validation passed: {len(rows)} unique entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())

