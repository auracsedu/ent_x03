import pytest

from problem_03 import my_join, my_replace


@pytest.mark.parametrize(
    "sep, items, expected",
    [
        (",", ["a", "b", "c"], "a,b,c"),
        (",", ["a"], "a"),
        (",", [], ""),
        ("", ["a", "b"], "ab"),
        ("--", ["1", "2", "3"], "1--2--3"),
        (",", ["", ""], ","),
        (" ", ["hello", "world"], "hello world"),
    ],
)
def test_my_join(sep, items, expected):
    assert my_join(sep, items) == expected


@pytest.mark.parametrize(
    "s, old, new, expected",
    [
        ("hello", "l", "L", "heLLo"),
        ("hello", "ll", "LL", "heLLo"),
        ("hello", "l", "", "heo"),
        ("aaa", "a", "bb", "bbbbbb"),
        ("aaa", "aa", "b", "ba"),
        ("aaaa", "aa", "b", "bb"),
        ("banana", "an", "AN", "bANANa"),
        ("hello", "z", "x", "hello"),
        ("abc", "abc", "x", "x"),
        ("", "a", "b", ""),
    ],
)
def test_my_replace(s, old, new, expected):
    assert my_replace(s, old, new) == expected
