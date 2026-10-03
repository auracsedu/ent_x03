import pytest

from problem_extra_01 import does_word_exist_in_board

BOARD_ABCE = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"],
]
BOARD_SPIRAL = [
    ["A", "B", "C"],
    ["H", "G", "D"],
    ["I", "F", "E"],
]
BOARD_GRID = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"],
]


@pytest.mark.parametrize(
    "board, word, expected",
    [
        (BOARD_ABCE, "ABCB", True),
        (BOARD_ABCE, "ABCCED", True),
        ([["A"]], "AAAAA", False),
        ([["A"]], "B", False),
        ([["A", "B", "C", "D", "E"]], "ABCDE", True),
        (BOARD_SPIRAL, "ABCDEFGHI", True),
        ([["A", "B"], ["C", "A"]], "ABACA", True),
        ([["B", "B"], ["B", "B"]], "A", False),
        (BOARD_GRID, "ABCFI", True),
        ([["A", "A"], ["A", "A"]], "AAAAAAAAAA", True),
        ([["A", "B"], ["C", "D"]], "", True),
    ],
)
def test_does_word_exist_in_board(board, word, expected):
    assert does_word_exist_in_board(board, word) is expected
