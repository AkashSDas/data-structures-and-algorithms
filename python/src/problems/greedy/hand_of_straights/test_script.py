import pytest

from src.problems.greedy.hand_of_straights.script import Solution


@pytest.mark.parametrize(
    "hand, groupSize, expected",
    [
        # ✅ Test Case 1: Standard Example (Possible grouping)
        ([1, 2, 3, 6, 2, 3, 4, 7, 8], 3, True),
        # Explanation: Possible groups → [1,2,3], [2,3,4], [6,7,8]
        # ✅ Test Case 2: Standard Example (Impossible grouping)
        ([1, 2, 3, 4, 5], 4, False),
        # Explanation: Cannot form groups of size 4 from given numbers.
        # ✅ Test Case 3: Single Element (Trivially Possible)
        ([5], 1, True),
        # Explanation: A single element can always form a group of 1.
        # ✅ Test Case 4: Repeated Elements, Consecutive Formation Possible
        ([1, 2, 3, 3, 4, 5], 3, True),
        # Explanation: Possible groups → [1,2,3], [3,4,5]
        # ✅ Test Case 5: Large Numbers, Still Possible
        ([1000000000, 1000000001, 1000000002], 3, True),
        # Explanation: Can be grouped as [1000000000, 1000000001, 1000000002]
        # ✅ Test Case 6: Large Numbers, Not Consecutive
        ([1000000000, 1000000002, 1000000004], 3, False),
        # Explanation: No three consecutive numbers exist.
        # ✅ Test Case 7: Large Input with Repeating Groups
        ([1, 2, 3] * 1000, 3, True),
        # Explanation: Groups of [1,2,3] can be formed 1000 times.
        # ✅ Test Case 8: GroupSize Larger Than Available Numbers
        ([1, 2, 3, 4, 5], 6, False),
        # Explanation: `groupSize` > `hand.length`, so it's impossible.
        # ✅ Test Case 9: Non-Consecutive Repeats
        ([1, 1, 2, 2, 3, 3], 3, True),
        # Explanation: Possible groups → [1,2,3], [1,2,3]
    ],
)
def test_isNStraightHand(hand, groupSize, expected):
    solution = Solution()
    assert solution.isNStraightHand(hand, groupSize) == expected
