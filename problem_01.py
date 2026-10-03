"""
문제 1. split 직접 만들기

문자열 s와 구분자 sep(한 글자)을 받아, s를 sep으로 자른 조각들의 리스트를
돌려주는 함수 my_split을 작성하세요. str.split()은 쓸 수 없습니다.

- 구분자가 연달아 나오면 그 사이에 빈 조각 ""이 들어갑니다.
- 문자열이 구분자로 시작하거나 끝나면 양 끝에도 빈 조각이 생깁니다.
- 구분자가 하나도 없으면 s 한 개만 담긴 리스트를 돌려줍니다.
- 빈 문자열은 [""]를 돌려줍니다. (조각이 0개가 아니라 1개입니다)

예시
    my_split("a,b,c", ",")  -> ["a", "b", "c"]
    my_split("a,,b", ",")   -> ["a", "", "b"]
    my_split("a,", ",")     -> ["a", ""]
    my_split(",a", ",")     -> ["", "a"]
    my_split("abc", ",")    -> ["abc"]
    my_split("", ",")       -> [""]

힌트
    - 지금 만들고 있는 조각을 담을 변수 piece = "" 를 하나 둡니다.
    - s를 한 글자씩 보면서, 구분자가 아니면 piece에 붙이고,
      구분자면 piece를 결과에 넣고 piece를 다시 "" 로 비웁니다.
    - 반복이 끝난 뒤 마지막 piece를 넣는 것을 잊지 마세요.
      이걸 빼먹으면 "a,b" 가 ["a"] 가 됩니다.
"""

from typing import List


def my_split(s: str, sep: str) -> List[str]:
    raise NotImplementedError
