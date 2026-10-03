"""
문제 2. 알파벳 첫 위치

소문자 문자열 s를 받아, a부터 z까지 각 알파벳이 s에서 처음 나타나는 인덱스를
담은 길이 26의 리스트를 반환하는 함수 alphabet_first_positions를 작성하세요.
s에 없는 알파벳은 -1로 표시합니다.

예시
    alphabet_first_positions("abcabc")
    -> [0, 1, 2, -1, -1, ..., -1]      # a는 0번, b는 1번, c는 2번, 나머지는 -1

    alphabet_first_positions("z")
    -> [-1, -1, ..., -1, 0]            # z만 0번, 나머지는 -1

    alphabet_first_positions("baekjoon")
    -> b는 0번, a는 1번, e는 2번, k는 3번, j는 4번, o는 5번, n은 7번, 나머지는 -1

힌트
    - "abcdefghijklmnopqrstuvwxyz" 를 한 글자씩 돌면서 결과를 하나씩 붙입니다.
    - str.find(문자) 는 그 문자가 처음 나오는 인덱스를, 없으면 -1을 돌려줍니다.
      (딱 이 문제가 원하는 동작입니다.)
"""

from typing import List


def alphabet_first_positions(s: str) -> List[int]:
    raise NotImplementedError
