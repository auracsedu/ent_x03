import pytest

from problem_02 import alphabet_first_positions


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
            # q   r   s   t   u   v   w   x   y   z
            + [-1] * 10,
        ),
    ],
)
def test_alphabet_first_positions(s, expected):
    assert alphabet_first_positions(s) == expected
