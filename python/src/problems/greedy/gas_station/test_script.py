import pytest
from src.problems.greedy.gas_station.script import Solution


@pytest.mark.parametrize(
    "gas, cost, expected",
    [
        # ✅ Test Case 1: Basic Example Case (Unique valid start)
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        #
        # ✅ Test Case 2: No Possible Circuit
        ([2, 3, 4], [3, 4, 3], -1),
        #
        # ✅ Test Case 3: Start from First Station
        ([4, 2, 3, 1, 5], [2, 2, 3, 1, 5], 0),
        # Explanation: Total gas >= total cost, and starting at index 0 ensures full traversal.
        #
        # ✅ Test Case 4: Large Values with Valid Start
        ([100, 200, 300, 400, 500], [200, 100, 300, 400, 400], 1),
        # Explanation: Best start is at index 1 since it allows surplus accumulation.
        #
        # ✅ Test Case 5: Large `n`, Impossible to Complete Circuit
        ([10000] * 100000, [10001] * 100000, -1),
    ],
)
def test_canCompleteCircuit(gas, cost, expected):
    solution = Solution()
    assert solution.canCompleteCircuit(gas, cost) == expected
