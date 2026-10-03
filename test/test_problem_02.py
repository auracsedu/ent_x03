import pytest

from problem_02 import alphabet_first_positions, my_find


@pytest.mark.parametrize(
    "s, target, expected",
    [
        ("hello", "l", 2),
        ("hello", "ll", 2),
        ("hello", "h", 0),
        ("hello", "o", 4),
        ("hello", "z", -1),
        ("hello", "hello", 0),
        ("hello", "helloo", -1),
        ("hello", "", 0),
        ("", "a", -1),
        ("", "", 0),
        ("aaa", "aa", 0),
        ("abcabc", "ca", 2),
    ],
)
def test_my_find(s, target, expected):
    assert my_find(s, target) == expected


@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcdefghijklmnopqrstuvwxyz", list(range(26))),
        ("aaaaa", [0] + [-1] * 25),
        ("z", [-1] * 25 + [0]),
        ("abcabc", [0, 1, 2] + [-1] * 23),
        ("", [-1] * 26),
        (
            "baekjoon",
            # a   b  c   d  e   f   g   h   i  j  k   l   m  n  o   p
            [1, 0, -1, -1, 2, -1, -1, -1, -1, 4, 3, -1, -1, 7, 5, -1]
            # q~z
            + [-1] * 10,
        ),
    ],
)
def test_alphabet_first_positions(s, expected):
    assert alphabet_first_positions(s) == expected
