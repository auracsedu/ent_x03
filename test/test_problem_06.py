import pytest

from problem_06 import hanoi


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, []),
        (1, [(1, 3)]),
        (2, [(1, 2), (1, 3), (2, 3)]),
        (3, [(1, 3), (1, 2), (3, 2), (1, 3), (2, 1), (2, 3), (1, 3)]),
    ],
)
def test_hanoi_moves(n, expected):
    assert hanoi(n) == expected


def test_hanoi_other_pegs():
    assert hanoi(2, 3, 1) == [(3, 2), (3, 1), (2, 1)]


@pytest.mark.parametrize("n", [1, 2, 3, 4, 5, 8, 10])
def test_hanoi_move_count(n):
    assert len(hanoi(n)) == 2**n - 1


@pytest.mark.parametrize("n", [1, 2, 3, 4, 5, 8])
def test_hanoi_moves_are_legal(n):
    # 원판은 큰 것이 1..n, 작은 것이 위. 규칙을 지키며 전부 3번 기둥으로 옮겨지는지 확인한다.
    pegs = {1: list(range(n, 0, -1)), 2: [], 3: []}
    for start, end in hanoi(n):
        assert pegs[start], f"빈 기둥 {start}에서 옮기려 했습니다"
        disk = pegs[start].pop()
        assert not pegs[end] or pegs[end][-1] > disk, "큰 원판을 작은 원판 위에 올렸습니다"
        pegs[end].append(disk)
    assert pegs[3] == list(range(n, 0, -1))
    assert pegs[1] == [] and pegs[2] == []
