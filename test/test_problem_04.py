import pytest

from problem_04 import swap_case


@pytest.mark.parametrize(
    "s, expected",
    [
        ("aBcDeF", "AbCdEf"),
        ("ABC", "abc"),
        ("xyz", "XYZ"),
        ("Hello World!", "hELLO wORLD!"),
        ("123abcDEF", "123ABCdef"),
        ("", ""),
    ],
)
def test_swap_case(s, expected):
    assert swap_case(s) == expected
