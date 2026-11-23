"""Command line for RepairMap: check, summary, show and list."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections.abc import Sequence

from repairmap import __version__
from repairmap.check import OUTCOME_CLASSES, RESULTS, SOURCE_TYPES, problems, summary
from repairmap.table import FIELDS, Row, load, select

LIST_COLUMNS = ("id", "agent", "phase", "n", "outcome_class", "result", "second_check")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="repairmap",
        description="A checked table of myelin repair trials in multiple sclerosis.",
    )
    parser.add_argument("--version", action="version", version=f"repairmap {__version__}")
    parser.add_argument("--table", metavar="CSV", help="read this file, not the built-in table")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("check", help="check every row against the schema; exit 1 on a fault")
    sub.add_parser("summary", help="print the headline counts")

    show = sub.add_parser("show", help="print one trial in full")
    show.add_argument("id", help="row id, for example clemastine-rebuild")

    lst = sub.add_parser("list", help="list trials, with optional filters")
    lst.add_argument("--agent", help="agent name contains this text")
    lst.add_argument("--mechanism", help="mechanism contains this text")
    lst.add_argument("--population", help="population contains this text")
    lst.add_argument("--registry-id", dest="registry_id", help="registry id contains this text")
    lst.add_argument("--phase", help="phase is exactly this, for example 2 or 1/2")
    lst.add_argument("--result", choices=RESULTS)
    lst.add_argument("--outcome-class", dest="outcome_class", choices=OUTCOME_CLASSES)
    lst.add_argument("--source-type", dest="source_type", choices=SOURCE_TYPES)
    lst.add_argument("--second-check", dest="second_check", choices=("yes", "no"))
    lst.add_argument("--format", choices=("table", "csv", "json"), default="table")
    return parser


def _table_text(rows: list[Row]) -> str:
    widths = {c: max(len(c), *(len(r[c]) for r in rows)) for c in LIST_COLUMNS}
    lines = ["  ".join(c.ljust(widths[c]) for c in LIST_COLUMNS).rstrip()]
    lines += ["  ".join(r[c].ljust(widths[c]) for c in LIST_COLUMNS).rstrip() for r in rows]
    return "\n".join(lines)


def _show_text(row: Row) -> str:
    width = max(len(f) for f in FIELDS)
    return "\n".join(f"{field.ljust(width)}  {row[field]}" for field in FIELDS)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        rows = load(args.table)
    except (OSError, ValueError) as err:
        print(f"repairmap: {err}", file=sys.stderr)
        return 2

    if args.command == "check":
        bad = problems(rows)
        for message in bad:
            print(message, file=sys.stderr)
        if bad:
            print(f"{len(bad)} problem(s) in {len(rows)} rows", file=sys.stderr)
            return 1
        print(f"ok: {len(rows)} rows")
        return 0

    if args.command == "summary":
        print(summary(rows))
        return 0

    if args.command == "show":
        match = [r for r in rows if r["id"] == args.id]
        if not match:
            print(f"repairmap: no trial with id {args.id!r}", file=sys.stderr)
            return 1
        print(_show_text(match[0]))
        return 0

    found = select(
        rows,
        agent=args.agent,
        mechanism=args.mechanism,
        population=args.population,
        registry_id=args.registry_id,
        phase=args.phase,
        result=args.result,
        outcome_class=args.outcome_class,
        source_type=args.source_type,
        second_check=args.second_check,
    )
    if args.format == "json":
        print(json.dumps(found, indent=2, ensure_ascii=False))
    elif args.format == "csv":
        writer = csv.DictWriter(sys.stdout, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(found)
    elif found:
        print(_table_text(found))
    print(f"{len(found)} of {len(rows)} trials", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
