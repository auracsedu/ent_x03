import pytest

from problem_04 import my_round


@pytest.mark.parametrize(
    "a, k, expected",
    [
        (5, 0, 10),
        (14, 0, 10),
        (15, 0, 20),
        (1234, 1, 1200),
        (1250, 1, 1300),
        (2.499, -1, 2),
        (2.5, -1, 3),
        (2.449, -2, 2.4),
        (2.451, -2, 2.5),
    ],
)
def test_my_round(a, k, expected):
    assert my_round(a, k) == expected
