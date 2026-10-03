import pytest

from problem_07 import combinations


@pytest.mark.parametrize(
    "items, r, expected",
    [
        ([1, 2, 3], 2, [[1, 2], [1, 3], [2, 3]]),
        ([1, 2, 3, 4], 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
        ([1, 2, 3], 1, [[1], [2], [3]]),
        ([1, 2, 3], 3, [[1, 2, 3]]),
        ([1, 2, 3], 0, [[]]),
        ([1, 2, 3], 4, []),
        ([], 0, [[]]),
        ([], 1, []),
        (["a", "b", "c"], 2, [["a", "b"], ["a", "c"], ["b", "c"]]),
        (
            [1, 2, 3, 4],
            3,
            [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]],
        ),
    ],
)
def test_combinations(items, r, expected):
    assert combinations(items, r) == expected


@pytest.mark.parametrize("n, r, count", [(5, 2, 10), (5, 3, 10), (6, 3, 20), (8, 4, 70)])
def test_combinations_count(n, r, count):
    assert len(combinations(list(range(n)), r)) == count


def test_combinations_does_not_modify_input():
    items = [1, 2, 3]
    combinations(items, 2)
    assert items == [1, 2, 3]
