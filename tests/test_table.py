"""The shipped table must be clean, and the loader must refuse a wrong header."""

import pytest

from repairmap import FIELDS, default_table, load, problems, select


def test_shipped_table_has_no_problems():
    assert problems(load()) == []


def test_default_table_is_the_checkout_file():
    path = default_table()
    assert path.name == "trials.csv"
    assert path.parent.name == "data"


def test_every_row_has_every_field():
    for row in load():
        assert tuple(row) == FIELDS


def test_load_refuses_a_wrong_header(tmp_path):
    bad = tmp_path / "t.csv"
    bad.write_text("id,agent\nx,y\n")
    with pytest.raises(ValueError, match="header"):
        load(bad)


def test_load_fills_short_rows_with_empty_strings(tmp_path):
    short = tmp_path / "t.csv"
    short.write_text(",".join(FIELDS) + "\nonly-id\n")
    (row,) = load(short)
    assert row["id"] == "only-id"
    assert row["second_check"] == ""


def test_select_exact_and_loose():
    rows = load()
    positive = select(rows, result="positive", outcome_class="biomarker")
    assert positive
    assert all(r["result"] == "positive" and r["outcome_class"] == "biomarker" for r in positive)
    assert {r["id"] for r in select(rows, agent="CLEMASTINE")} >= {"clemastine-rebuild"}
    assert select(rows, phase="no such phase") == []


def test_select_rejects_unknown_column():
    with pytest.raises(KeyError):
        select(load(), colour="red")
