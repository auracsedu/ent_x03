"""
문제 2. find 직접 만들기

함수 두 개를 작성하세요.

(1) my_find(s, target)
    문자열 s 안에서 target이 처음 나타나는 인덱스를 돌려줍니다.
    없으면 -1을 돌려줍니다. str.find(), str.index(), in 은 쓸 수 없습니다.

    - target은 한 글자가 아니어도 됩니다. ("ll" 처럼 두 글자 이상)
    - target이 빈 문자열이면 0을 돌려줍니다.

    my_find("hello", "l")  -> 2
    my_find("hello", "ll") -> 2
    my_find("hello", "z")  -> -1
    my_find("hello", "")   -> 0
    my_find("", "a")       -> -1

(2) alphabet_first_positions(s)
    소문자 문자열 s에서 a부터 z까지 각 알파벳이 처음 나타나는 인덱스를 담은
    길이 26의 리스트를 돌려줍니다. s에 없는 알파벳은 -1로 표시합니다.
    (1)에서 만든 my_find를 쓰세요.

    alphabet_first_positions("abcabc")
        -> [0, 1, 2, -1, -1, ..., -1]   # a는 0번, b는 1번, c는 2번, 나머지 -1
    alphabet_first_positions("z")
        -> [-1, -1, ..., -1, 0]         # z만 0번
    alphabet_first_positions("baekjoon")
        -> b는 0번, a는 1번, e는 2번, k는 3번, j는 4번, o는 5번, n은 7번, 나머지 -1

힌트
    - my_find: 시작 위치 i를 0부터 늘려 가면서, s[i:i + len(target)] 이
      target과 같은지 봅니다. 같아지면 그 i가 답입니다.
      i는 어디까지 커질 수 있는지 생각해 보세요. (len(s) - len(target) 까지)
    - alphabet_first_positions: "abcdefghijklmnopqrstuvwxyz" 를 한 글자씩
      돌면서 my_find(s, 그_글자) 를 결과에 붙이면 끝납니다.
"""

from typing import List


def my_find(s: str, target: str) -> int:
    raise NotImplementedError


def alphabet_first_positions(s: str) -> List[int]:
    raise NotImplementedError
