"""EX07 - Dictionary Functions."""

__author__ = "730558551"

from dictionary import invert
from dictionary import count
from dictionary import favorite_color
import pytest


def test_empty_dict() -> None:
    """Tests edge case of empty list."""
    dict_x: dict[str, str] = {}
    assert invert(dict_x) == {}


def test_repeat_keys() -> None:
    """Checks for repeated keys."""
    dict_1: dict[str, str] = {}
    with pytest.raises(KeyError):
        dict_1 = {"aa": "bb", "cc": "dd", "ee": "ff", "pip": "bb"}
        invert(dict_1)


def test_normal_keys() -> None:
    """Testing for dictionary without repeats."""
    dict_ie: dict[str, str] = {"aa": "bb", "cc": "dd", "ee": "ff", "gg": "hh"}
    assert invert(dict_ie) == {"bb": "aa", "dd": "cc", "ff": "ee", "hh": "gg"}


def test_sev_modes() -> None:
    """Tests a list with several modes."""
    list_x: list[str] = ["a", "b", "c", "a", "b"]
    assert count(list_x) == {"a": 2, "b": 2, "c": 1}


def test_empty_list() -> None:
    """Tests edge case for empty list."""
    list_x: list[str] = []
    assert count(list_x) == {}


def test_normal_list() -> None:
    """Testing a normal list with no modes."""
    list_x: list[str] = ["a", "b", "c", "d"]
    assert count(list_x) == {"a": 1, "b": 1, "c": 1, "d": 1}


def test_sing_mode() -> None:
    """Tests dict with singular mode."""
    dict_x: dict[str, str] = {"p1": "red", "p2": "red", "p3": "red", "p4": "blue"}
    assert favorite_color(dict_x) == "red"


def test_modeless() -> None:
    """Testing dict with no mode."""
    dict_x: dict[str, str] = {"p1": "green", "p2": "red", "p3": "orange", "p4": "blue"}
    assert favorite_color(dict_x) == "green"


def test_empty_dict_two() -> None:
    """Tests edge case of empty list."""
    dict_x: dict[str, str] = {}
    assert favorite_color(dict_x) == ""