"""
문제 9. 한 줄에서 단어 찾기 (백트래킹)

각 칸에 알파벳 한 글자가 들어 있는 1차원 리스트 line이 주어집니다.
어떤 칸에서 시작해 왼쪽 또는 오른쪽 옆 칸으로만 움직이면서 글자를 이어
문자열 word를 만들 수 있으면 True, 없으면 False를 돌려주는 함수
does_word_exist_in_line을 작성하세요.

- 한 칸에서 갈 수 있는 곳은 바로 왼쪽과 바로 오른쪽, 두 군데입니다.
- 왔던 길을 되돌아가도 되지만, 같은 칸을 두 번 쓸 수는 없습니다.
- word가 빈 문자열이면 True입니다.

예시
    line = ["A", "B", "C", "D"]

    does_word_exist_in_line(line, "ABC")  -> True    # 0 -> 1 -> 2
    does_word_exist_in_line(line, "DCBA") -> True    # 3 -> 2 -> 1 -> 0
    does_word_exist_in_line(line, "AC")   -> False   # A와 C는 옆칸이 아님
    does_word_exist_in_line(line, "ABA")  -> False   # A가 하나뿐인데 두 번 필요
    does_word_exist_in_line(line, "CBAD") -> False   # A 다음 D로 갈 수 없음

    does_word_exist_in_line(["A", "B", "A"], "ABA")  -> True   # 0 -> 1 -> 2
    does_word_exist_in_line(["A"], "AA")             -> False

재귀로 생각하는 법
    문제 7, 8과 비슷하지만 "다음에 무엇을 고르는가"가 위치로 바뀝니다.

    재귀 함수 하나를 만듭니다.
        go(i, k) = "line[i]에서 시작해 word[k]부터 끝까지 만들 수 있는가?"

        1) i가 리스트 밖이거나, 이미 쓴 칸이거나, line[i] != word[k] 면 False
        2) k가 word의 마지막 글자였다면 True (다 만들었습니다)
        3) 아니면 왼쪽(i-1)과 오른쪽(i+1) 두 군데로 go(..., k+1)을 불러 보고
           하나라도 True면 True

    시작 칸은 어디든 될 수 있으므로, 모든 i에 대해 go(i, 0)을 시도합니다.

힌트
    - "이미 쓴 칸"은 인덱스를 set에 넣어 기록합니다.
    - 중요: 3)에서 재귀를 부르고 돌아온 뒤에는 i를 set에서 다시 빼야 합니다.
      이 경로에서만 막힌 것이고, 다른 시작점/다른 경로에서는 쓸 수 있는
      칸이기 때문입니다. (문제 8의 "다른 방법" 설명과 같은 이야기입니다.)
    - 돌려주는 값은 True / False 여야 합니다. (테스트가 is True 로 확인합니다.)

    extra 문제는 이것을 2차원 보드에서 하는 문제입니다.
    갈 수 있는 방향이 2개에서 4개(상하좌우)로 늘고, 위치가 i 하나에서
    (r, c) 두 개로 늘어나는 것 말고는 똑같습니다.
"""

from typing import List


def does_word_exist_in_line(line: List[str], word: str) -> bool:
    raise NotImplementedError
