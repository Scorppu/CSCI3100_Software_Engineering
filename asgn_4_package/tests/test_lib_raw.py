import pytest

from asgn_4_package import lib_raw


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("", "", 0),
        ("abc", "def", 0),
        ("abc", "abc", 3),
        ("abcde", "ace", 1),
        ("a", "a", 1),
        ("abcdef", "def", 3),
    ]
)
def test_lcs_cases(a, b, expected):
    assert lib_raw.longest_common_substr(a, b) == expected
