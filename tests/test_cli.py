"""The command line: exit codes, filters and output formats."""

import csv
import io
import json

from repairmap.cli import main
from repairmap.table import FIELDS, load


def test_check_passes_on_the_shipped_table(capsys):
    assert main(["check"]) == 0
    assert capsys.readouterr().out.startswith("ok: ")


def test_check_fails_on_a_broken_table(tmp_path, capsys):
    bad = tmp_path / "t.csv"
    bad.write_text(",".join(FIELDS) + "\n" + ",".join(["x"] * len(FIELDS)) + "\n")
    assert main(["--table", str(bad), "check"]) == 1
    assert "outcome_class 'x'" in capsys.readouterr().err


def test_missing_table_exits_2(tmp_path, capsys):
    assert main(["--table", str(tmp_path / "none.csv"), "summary"]) == 2
    assert "repairmap:" in capsys.readouterr().err


def test_summary_prints_row_count(capsys):
    assert main(["summary"]) == 0
    assert f"rows: {len(load())}" in capsys.readouterr().out


def test_show_known_and_unknown(capsys):
    assert main(["show", "clemastine-rebuild"]) == 0
    out = capsys.readouterr().out
    assert "ReBUILD" in out
    assert out.count("\n") == len(FIELDS)
    assert main(["show", "no-such-trial"]) == 1


def test_list_filters_and_formats(capsys):
    assert main(["list", "--result", "positive", "--outcome-class", "biomarker"]) == 0
    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[0].startswith("id")
    assert all("positive" in line for line in lines[1:])
    assert f"{len(lines) - 1} of {len(load())} trials" in captured.err

    assert main(["list", "--agent", "clemastine", "--format", "json"]) == 0
    rows = json.loads(capsys.readouterr().out)
    assert rows and all("clemastine" in r["agent"] for r in rows)

    assert main(["list", "--result", "harm", "--format", "csv"]) == 0
    parsed = list(csv.DictReader(io.StringIO(capsys.readouterr().out)))
    assert parsed and all(r["result"] == "harm" for r in parsed)
