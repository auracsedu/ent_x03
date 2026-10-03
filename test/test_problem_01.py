import pytest

from problem_01 import my_split


@pytest.mark.parametrize(
    "s, sep, expected",
    [
        ("a,b,c", ",", ["a", "b", "c"]),
        ("a,,b", ",", ["a", "", "b"]),
        ("a,", ",", ["a", ""]),
        (",a", ",", ["", "a"]),
        (",", ",", ["", ""]),
        ("abc", ",", ["abc"]),
        ("", ",", [""]),
        ("a b c", " ", ["a", "b", "c"]),
        ("1-2-3-4", "-", ["1", "2", "3", "4"]),
    ],
)
def test_my_split(s, sep, expected):
    assert my_split(s, sep) == expected
