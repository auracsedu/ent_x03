import pytest

from problem_09 import does_word_exist_in_line


@pytest.mark.parametrize(
    "line, word, expected",
    [
        (["A", "B", "C", "D"], "ABC", True),
        (["A", "B", "C", "D"], "DCBA", True),
        (["A", "B", "C", "D"], "BCD", True),
        (["A", "B", "C", "D"], "AC", False),
        (["A", "B", "C", "D"], "ABA", False),
        (["A", "B", "C", "D"], "CBAD", False),
        (["A", "B", "C", "D"], "", True),
        (["A", "B", "C", "D"], "Z", False),
        (["A", "B", "A"], "ABA", True),
        (["A", "B", "A"], "ABAB", False),
        (["A", "B", "A", "B"], "ABAB", True),
        (["A"], "A", True),
        (["A"], "AA", False),
        (["A", "A", "A"], "AAA", True),
        (["A", "B", "C"], "BA", True),
        (["A", "B", "C"], "BCA", False),
    ],
)
def test_does_word_exist_in_line(line, word, expected):
    assert does_word_exist_in_line(line, word) is expected
