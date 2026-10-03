import pytest

from problem_01 import nth_prime


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 2),
        (2, 3),
        (3, 5),
        (5, 11),
        (6, 13),
        (10, 29),
        (100, 541),
        (1000, 7919),
        (10000, 104729),
    ],
)
def test_nth_prime(n, expected):
    assert nth_prime(n) == expected
