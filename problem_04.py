"""
문제 4. 대소문자 바꾸기

문자열 s를 받아 대문자는 소문자로, 소문자는 대문자로 바꾼 새 문자열을
반환하는 함수 swap_case를 작성하세요. 알파벳이 아닌 문자는 그대로 둡니다.

예시
    swap_case("aBcDeF")       -> "AbCdEf"
    swap_case("Hello World!") -> "hELLO wORLD!"
    swap_case("123abcDEF")    -> "123ABCdef"

힌트
    - 빈 문자열에서 시작해 한 글자씩 붙여 나갑니다.
    - str.isupper(), str.islower(), str.upper(), str.lower() 를 씁니다.
    - 파이썬에는 이걸 바로 해 주는 str.swapcase() 가 있지만,
      이 문제에서는 쓰지 말고 직접 만들어 보세요.
"""


def swap_case(s: str) -> str:
    raise NotImplementedError
