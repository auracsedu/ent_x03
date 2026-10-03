"""
문제 3. join과 replace 직접 만들기

함수 두 개를 작성하세요. 문제 1(my_split)의 짝이 되는 문제입니다.

(1) my_join(sep, items)
    문자열 리스트 items의 원소들을 sep으로 이어 붙인 하나의 문자열을
    돌려줍니다. str.join()은 쓸 수 없습니다.

    my_join(",", ["a", "b", "c"])  -> "a,b,c"
    my_join(",", ["a"])            -> "a"
    my_join(",", [])               -> ""
    my_join("", ["a", "b"])        -> "ab"
    my_join("--", ["1", "2", "3"]) -> "1--2--3"

    주의: 구분자는 조각 "사이"에만 들어갑니다. 끝에 붙으면 안 됩니다.
          my_join(",", ["a", "b"]) 가 "a,b," 가 되면 틀립니다.

(2) my_replace(s, old, new)
    문자열 s에서 old를 모두 찾아 new로 바꾼 새 문자열을 돌려줍니다.
    str.replace()는 쓸 수 없습니다.

    - old는 빈 문자열이 아닙니다. new는 빈 문자열일 수 있습니다.
    - 왼쪽부터 찾고, 바꾼 부분은 다시 검사하지 않습니다.
      ("aaa" 에서 "aa" 를 "b" 로 바꾸면 "ba" 입니다. "b" + 남은 "a")
    - old가 없으면 s를 그대로 돌려줍니다.

    my_replace("hello", "l", "L")     -> "heLLo"
    my_replace("hello", "ll", "LL")   -> "heLLo"
    my_replace("hello", "l", "")      -> "heo"
    my_replace("aaa", "a", "bb")      -> "bbbbbb"
    my_replace("aaa", "aa", "b")      -> "ba"
    my_replace("banana", "an", "AN")  -> "bANANa"
    my_replace("hello", "z", "x")     -> "hello"

힌트
    - my_join: 첫 조각을 먼저 넣고, 두 번째 조각부터 sep을 앞에 붙여 가며
      더합니다. 또는 "지금이 첫 조각인가"를 확인하는 방법도 있습니다.
      items가 비어 있으면 ""입니다.
    - my_replace: 위치 i를 0부터 움직이면서
        s[i:i + len(old)] == old 이면  -> 결과에 new를 붙이고 i를 len(old)만큼 건너뜀
        아니면                          -> 결과에 s[i] 한 글자를 붙이고 i를 1 늘림
      while 반복문으로 i를 직접 움직이는 것이 for보다 편합니다.
      (문제 2의 my_find와 비교해 보세요. 같은 "슬라이싱으로 비교하기"입니다.)
"""

from typing import List


def my_join(sep: str, items: List[str]) -> str:
    raise NotImplementedError


def my_replace(s: str, old: str, new: str) -> str:
    raise NotImplementedError
