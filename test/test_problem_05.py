import pytest

from problem_05 import flatten


@pytest.mark.parametrize(
    "items, expected",
    [
        ([1, 2, 3], [1, 2, 3]),
        ([1, [2, 3], 4], [1, 2, 3, 4]),
        ([1, [2, [3, [4]]]], [1, 2, 3, 4]),
        ([], []),
        ([[], [[]], []], []),
        ([[1, 2], [3, [4, 5]]], [1, 2, 3, 4, 5]),
        ([[[[[7]]]]], [7]),
        ([1, [], 2, [[]], 3], [1, 2, 3]),
        ([[3, 2], [1]], [3, 2, 1]),
    ],
)
def test_flatten(items, expected):
    assert flatten(items) == expected


def test_flatten_does_not_modify_input():
    items = [1, [2, [3]], 4]
    flatten(items)
    assert items == [1, [2, [3]], 4]
