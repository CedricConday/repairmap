"""Each schema rule must fire on a row that breaks it, and only then."""

import pytest

from repairmap.check import problems, summary
from repairmap.table import FIELDS

GOOD = {
    "id": "drug-trial",
    "agent": "drug",
    "trial": "TRIAL",
    "registry_id": "NCT00000000",
    "mechanism": "some mechanism",
    "phase": "2",
    "n": "50",
    "population": "relapsing MS",
    "primary_outcome": "VEP latency",
    "outcome_class": "biomarker",
    "result": "positive",
    "effect": "",
    "source": "PMID 1",
    "source_type": "paper",
    "source_date": "2020",
    "second_check": "no",
    "checked_on": "",
    "check_note": "source not reachable",
}


def row(**changes):
    out = {**GOOD, **changes}
    assert tuple(out) == FIELDS
    return out


def test_good_row_is_clean():
    assert problems([row()]) == []


@pytest.mark.parametrize(
    ("changes", "expected"),
    [
        ({"agent": ""}, "empty agent"),
        ({"source": ""}, "empty source"),
        ({"id": "Drug Trial"}, "id must be"),
        ({"outcome_class": "imaging"}, "outcome_class"),
        ({"result": "won"}, "result"),
        ({"source_type": "blog"}, "source_type"),
        ({"n": "about 50"}, "n 'about 50'"),
        ({"source_date": "May 2020"}, "source_date"),
        ({"second_check": "maybe"}, "second_check"),
        ({"effect": " padded"}, "stray whitespace in effect"),
        ({"checked_on": "23 Nov 2026"}, "checked_on"),
        ({"second_check": "yes"}, "without checked_on"),
        ({"check_note": ""}, "without a check_note"),
    ],
)
def test_each_rule_fires(changes, expected):
    found = problems([row(**changes)])
    assert len(found) == 1
    assert expected in found[0]
    assert found[0].startswith("line 2 ")


def test_duplicate_id_is_reported_on_the_second_row():
    found = problems([row(), row()])
    assert found == ["line 3 (drug-trial): duplicate id"]


def test_empty_n_is_allowed():
    assert problems([row(n="")]) == []


def test_summary_counts():
    rows = [
        row(),
        row(
            id="b",
            result="negative",
            outcome_class="functional",
            second_check="yes",
            checked_on="2026-11-23",
        ),
        row(id="c", agent="other", result="ongoing"),
    ]
    text = summary(rows)
    assert "rows: 3   agents: 2" in text
    assert "with a result on the primary outcome: 2" in text
    assert "biomarker primary: positive 1" in text
    assert "functional primary: negative 1" in text
    assert "without one: 1" in text
    assert "  ongoing 1" in text
    assert "checked a second time: 1 of 3" in text
