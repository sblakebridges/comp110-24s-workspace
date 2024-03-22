"""Test my garden functions."""

__author__ = "730643380"

from lessons.garden.garden_helpers import add_by_date, add_by_kind, lookup_by_kind_and_date


def test_edge_add_by_kind() -> None:
    """Edge case test for add_by_kind."""
    garden_test = {"flower": ["rose", "tulip", "sunflower"]}
    add_by_kind(garden_test, "", "")
    assert garden_test == {"flower": ["rose", "tulip", "sunflower"], "": [""]}


def test_case_add_by_kind() -> None:
    """Regular case test for add_by_kind."""
    garden_test = {"flower": ["rose", "tulip"]}
    add_by_kind(garden_test, "flower", "carnation")
    assert garden_test == {"flower": ["rose", "tulip", "carnation"]}


def test_edge_add_by_date() -> None:
    """Edge case test for add_by_date."""
    garden_test = {"December": ["hydrangea"], "January": ["corn"]}
    add_by_date(garden_test, "", "")
    assert garden_test == {"December": ["hydrangea"], "January": ["corn"], "": [""]}


def test_case_add_by_date() -> None:
    """Regular case test for add_by_date."""
    garden_test = {"July": ["sunflower"], "April": ["lettuce"]}
    add_by_date(garden_test, "March", "greenpea")
    assert garden_test == {"July": ["sunflower"], "April": ["lettuce"], "March": ["greenpea"]}


def test_edge_lookup_by_kind_and_date() -> None:
    """Edge case for lookup_by_kind_and_date."""
    assert lookup_by_kind_and_date({}, {"May": ["orchid", "apple"]}, "flower", "May") == "No flowers to plant in May."


def test_case_lookup_by_kind_and_date() -> None:
    """Regular case for lookup_by_kind_and_date."""
    assert lookup_by_kind_and_date({"flower": ["Hydrangea", "Rose"], "vegetable": ["Carrot"]}, {"January": ["Rose", "Carrot", "Hydrangea"]}, "flower", "January") == "flowers to plant in January: ['Hydrangea', 'Rose']"