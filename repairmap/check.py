"""Check the trial table against its schema and count what it holds."""

from __future__ import annotations

import re
from collections import Counter

from repairmap.table import Row

OUTCOME_CLASSES = ("biomarker", "functional", "safety", "target_engagement")
RESULTS = (
    "positive",
    "mixed",
    "negative",
    "harm",
    "unclear",
    "safety_only",
    "ongoing",
    "not_started",
    "stopped",
    "not_reported",
)
SOURCE_TYPES = ("paper", "registry", "conference", "company", "review")
REQUIRED = ("id", "agent", "mechanism", "phase", "primary_outcome", "result", "source")

# Results that make a call on the primary outcome, as opposed to a status.
EFFICACY_RESULTS = ("positive", "mixed", "negative", "harm")

ID_PATTERN = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
DATE_PATTERN = re.compile(r"\d{4}(-\d{2}(-\d{2})?)?")
DAY_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2}")


def problems(rows: list[Row]) -> list[str]:
    """Return one message per schema fault. An empty list means the table is clean."""
    out: list[str] = []
    seen: set[str] = set()
    for line, row in enumerate(rows, start=2):
        tag = f"line {line} ({row.get('id') or '?'})"
        for key in REQUIRED:
            if not row[key].strip():
                out.append(f"{tag}: empty {key}")
        for key, value in row.items():
            if value != value.strip():
                out.append(f"{tag}: stray whitespace in {key}")
        if row["id"] and not ID_PATTERN.fullmatch(row["id"]):
            out.append(f"{tag}: id must be lower-case words joined by hyphens")
        if row["id"] in seen:
            out.append(f"{tag}: duplicate id")
        seen.add(row["id"])
        if row["outcome_class"] not in OUTCOME_CLASSES:
            out.append(f"{tag}: outcome_class {row['outcome_class']!r}")
        if row["result"] not in RESULTS:
            out.append(f"{tag}: result {row['result']!r}")
        if row["source_type"] not in SOURCE_TYPES:
            out.append(f"{tag}: source_type {row['source_type']!r}")
        if row["n"] and not row["n"].isdigit():
            out.append(f"{tag}: n {row['n']!r}")
        if row["source_date"] and not DATE_PATTERN.fullmatch(row["source_date"]):
            out.append(f"{tag}: source_date {row['source_date']!r}")
        if row["second_check"] not in {"yes", "no"}:
            out.append(f"{tag}: second_check {row['second_check']!r}")
        if row["checked_on"] and not DAY_PATTERN.fullmatch(row["checked_on"]):
            out.append(f"{tag}: checked_on {row['checked_on']!r}")
        if row["second_check"] == "yes" and not (row["checked_on"] and row["check_note"]):
            out.append(f"{tag}: second_check is yes without checked_on and check_note")
        if row["second_check"] == "no" and not row["check_note"]:
            out.append(f"{tag}: second_check is no without a check_note giving the reason")
    return out


def summary(rows: list[Row]) -> str:
    """Return the headline counts as plain text."""
    done = [r for r in rows if r["result"] in EFFICACY_RESULTS]
    by = Counter((r["outcome_class"], r["result"]) for r in done)
    status = Counter(r["result"] for r in rows if r["result"] not in EFFICACY_RESULTS)
    lines = [
        f"rows: {len(rows)}   agents: {len({r['agent'] for r in rows})}",
        f"with a result on the primary outcome: {len(done)}",
    ]
    for cls in OUTCOME_CLASSES:
        parts = [f"{res} {by[(cls, res)]}" for res in EFFICACY_RESULTS if by[(cls, res)]]
        if parts:
            lines.append(f"  {cls} primary: " + ", ".join(parts))
    rest = [f"{res} {status[res]}" for res in RESULTS if status[res]]
    if rest:
        lines.append(f"without one: {len(rows) - len(done)}")
        lines.append("  " + ", ".join(rest))
    checked = sum(r["second_check"] == "yes" for r in rows)
    lines.append(f"checked a second time: {checked} of {len(rows)}")
    return "\n".join(lines)
