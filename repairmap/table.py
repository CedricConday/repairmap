"""Find, load and filter the trial table.

The table is one CSV file, ``data/trials.csv``. It is the only source of
truth: nothing generates it, and every edit is made to the file itself.
"""

from __future__ import annotations

import csv
from collections.abc import Iterable
from importlib import resources
from pathlib import Path

FIELDS = (
    "id",
    "agent",
    "trial",
    "registry_id",
    "mechanism",
    "phase",
    "n",
    "population",
    "primary_outcome",
    "outcome_class",
    "result",
    "effect",
    "source",
    "source_type",
    "source_date",
    "second_check",
    "checked_on",
    "check_note",
)

Row = dict[str, str]


def default_table() -> Path:
    """Return the path of the table that ships with this copy of the code.

    A source checkout keeps the file in ``data/`` beside the package. An
    installed wheel carries the same file as ``repairmap/data/trials.csv``.
    """
    checkout = Path(__file__).resolve().parent.parent / "data" / "trials.csv"
    if checkout.is_file():
        return checkout
    return Path(str(resources.files("repairmap") / "data" / "trials.csv"))


def load(path: Path | str | None = None) -> list[Row]:
    """Read the table. Missing cells become empty strings."""
    table = Path(path) if path is not None else default_table()
    with table.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        header = tuple(reader.fieldnames or ())
        rows = [{k: (v or "") for k, v in row.items() if k is not None} for row in reader]
    if header != FIELDS:
        raise ValueError(f"{table}: header is {list(header)}, expected {list(FIELDS)}")
    return rows


def select(rows: Iterable[Row], **filters: str | None) -> list[Row]:
    """Keep the rows that match every given filter.

    A filter on ``agent``, ``mechanism``, ``population``, ``trial`` or
    ``registry_id`` matches
    when the text appears anywhere in the cell, ignoring case. Every other
    column must match exactly.
    """
    loose = {"agent", "mechanism", "population", "trial", "registry_id"}
    wanted = {k: v for k, v in filters.items() if v is not None}
    unknown = set(wanted) - set(FIELDS)
    if unknown:
        raise KeyError(f"not a column: {sorted(unknown)}")
    out = []
    for row in rows:
        for key, value in wanted.items():
            cell = row[key]
            if key in loose:
                if value.lower() not in cell.lower():
                    break
            elif cell != value:
                break
        else:
            out.append(row)
    return out
