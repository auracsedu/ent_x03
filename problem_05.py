"""
문제 5. 보드에서 단어 찾기 (재사용 가능)

각 칸에 알파벳 한 글자가 들어 있는 2차원 리스트 board가 주어집니다.
인접한 칸들을 이어서 문자열 word를 만들 수 있으면 True, 없으면 False를
반환하는 함수 does_word_exist_in_board를 작성하세요.

- 인접한 칸은 상하좌우로 붙어 있는 칸입니다. 대각선은 인접하지 않습니다.
- 한 번 쓴 칸을 다시 써도 됩니다. (문제 6과 다른 점입니다.)
- word가 빈 문자열이면 True입니다.

예시
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]

    does_word_exist_in_board(board, "ABCB")  -> True
        A(0,0) -> B(0,1) -> C(0,2) -> B(0,1)
        B를 두 번 쓰지만, 이 문제에서는 허용됩니다.

    does_word_exist_in_board([["A"]], "AAAAA") -> False
        혼자 있는 A는 자기 자신과 인접하지 않으므로 이어 붙일 수 없습니다.

힌트
    - 모든 칸을 시작점으로 한 번씩 시도해 봅니다.
    - 재귀 함수를 하나 만듭니다: search(r, c, i) 는
      "board[r][c]에서 시작해서 word[i:]를 만들 수 있는가?" 를 답합니다.
      1) r, c가 보드 밖이거나 board[r][c] != word[i] 면 False
      2) i가 word의 마지막 글자였다면 True
      3) 아니면 상하좌우 네 방향에 대해 search(..., i + 1) 중 하나라도
         True면 True
    - 반환값은 True / False 여야 합니다. (테스트가 is True 로 확인합니다.)
"""

from typing import List


def does_word_exist_in_board(board: List[List[str]], word: str) -> bool:
    raise NotImplementedError
