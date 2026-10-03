import pytest

from problem_08 import permutations


@pytest.mark.parametrize(
    "items, expected",
    [
        ([], [[]]),
        ([1], [[1]]),
        ([1, 2], [[1, 2], [2, 1]]),
        (
            [1, 2, 3],
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        ),
        (
            ["a", "b", "c"],
            [
                ["a", "b", "c"],
                ["a", "c", "b"],
                ["b", "a", "c"],
                ["b", "c", "a"],
                ["c", "a", "b"],
                ["c", "b", "a"],
            ],
        ),
    ],
)
def test_permutations(items, expected):
    assert permutations(items) == expected


@pytest.mark.parametrize("n, count", [(1, 1), (2, 2), (3, 6), (4, 24), (5, 120), (6, 720)])
def test_permutations_count(n, count):
    assert len(permutations(list(range(n)))) == count


def test_permutations_all_different():
    result = permutations([1, 2, 3, 4])
    assert len({tuple(p) for p in result}) == 24


def test_permutations_does_not_modify_input():
    items = [1, 2, 3]
    permutations(items)
    assert items == [1, 2, 3]
