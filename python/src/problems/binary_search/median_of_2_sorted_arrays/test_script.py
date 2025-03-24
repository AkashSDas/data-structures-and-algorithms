import pytest

from src.problems.binary_search.median_of_2_sorted_arrays.script import Solution


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([1, 3], [2], 2.0),  # Odd length case
        ([1, 2], [3, 4], 2.5),  # Even length case
        ([0, 0], [0, 0], 0.0),  # All elements same
        ([], [1], 1.0),  # One empty array
        ([2], [], 2.0),  # Other empty array
        ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5.5),  # Larger arrays
        ([1, 3, 8], [7, 9, 10, 11], 8.0),  # Partition in different locations
    ],
)
def test_find_median_sorted_arrays(nums1, nums2, expected):
    sol = Solution()
    assert sol.findMedianSortedArrays(nums1, nums2) == pytest.approx(expected, rel=1e-5)


if __name__ == "__main__":
    pytest.main()
