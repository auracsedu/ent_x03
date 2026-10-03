"""
문제 6. 보드에서 단어 찾기 (재사용 불가)

문제 5와 거의 같습니다. 단, 한 번 쓴 칸은 다시 쓸 수 없습니다.

- 인접한 칸은 상하좌우로 붙어 있는 칸입니다. 대각선은 인접하지 않습니다.
- 한 경로 안에서 같은 칸을 두 번 지나갈 수 없습니다.
- word가 빈 문자열이면 True입니다.

예시
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]

    does_word_exist_in_board(board, "ABCB")   -> False
        B(0,1)를 두 번 써야 하므로 만들 수 없습니다.

    does_word_exist_in_board(board, "ABCCED") -> True
        A(0,0) -> B(0,1) -> C(0,2) -> C(1,2) -> E(2,2) -> D(2,1)

힌트
    - 문제 5의 코드에서 "지금 경로에서 이미 쓴 칸"을 기억하기만 하면 됩니다.
    - 방문한 칸의 (r, c)를 set에 넣어 두고, 재귀로 들어가기 전에
      set에 있는지 확인하세요.
    - 중요: 재귀에서 돌아온 뒤에는 그 칸을 set에서 다시 빼 주어야 합니다.
      (이 경로에서만 막힌 것이고, 다른 경로에서는 쓸 수 있는 칸입니다.)
      이렇게 되돌리는 방식을 백트래킹이라고 합니다.
"""

from typing import List


def does_word_exist_in_board(board: List[List[str]], word: str) -> bool:
    raise NotImplementedError
