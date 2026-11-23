"""docs/EXCLUDED.md and the table must not contradict each other."""

import re
from pathlib import Path

from repairmap import load

DOC = Path(__file__).resolve().parent.parent / "docs" / "EXCLUDED.md"
ROW = re.compile(r"^\| (NCT\d{8}) \| .* \| (in the table|excluded) \| (.*) \|$")


def reconciled():
    found = [ROW.match(line) for line in DOC.read_text(encoding="utf-8").splitlines()]
    return [m.groups() for m in found if m]


def test_every_registry_hit_is_reconciled_once():
    ids = [nct for nct, _, _ in reconciled()]
    assert len(ids) == 66
    assert len(set(ids)) == len(ids)


def test_reconciliation_agrees_with_the_table():
    rows = {r["id"]: r for r in load()}
    cited = " ".join(r["registry_id"] + " " + r["source"] for r in rows.values())
    for nct, status, detail in reconciled():
        if status == "in the table":
            row = rows[detail.strip("`")]
            assert nct in row["registry_id"] + " " + row["source"]
        else:
            assert nct not in cited, f"{nct} is excluded but cited in the table"
