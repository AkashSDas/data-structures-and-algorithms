import pytest

from src.problems.dp_1d.decode_ways.script import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("12", 2),  # "AB" (1 2) or "L" (12)
        ("226", 3),  # "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6)
        ("06", 0),  # Leading zero makes it invalid
        ("11106", 2),  # "AAJF" (1,1,10,6) or "KJF" (11,10,6)
        ("0", 0),  # Single zero is invalid
        ("10", 1),  # "J" (10)
        ("27", 1),  # "BG" (2,7) since "27" is not "AA"
        ("101", 1),  # "JA" (10,1), "0" is an invalid start
        ("100", 0),  # "100" has no valid decoding
        ("110", 1),  # "J" (10) cannot be paired with "0"
        ("111", 3),  # "AAA" (1,1,1), "KA" (11,1), or "AK" (1,11)
        (
            "123456",
            3,
        ),  # "ABCDEF" (1,2,3,4,5,6), "AWDEF" (1,23,4,5,6), "LCDEF" (12,3,4,5,6)
        ("999", 1),  # Only one way: "III" (9,9,9)
        ("2626", 4),  # "ZBF", "ZB", "VF", "VBF"
    ],
)
def test_num_decodings(s, expected):
    sol = Solution()
    assert sol.numDecodings(s) == expected
