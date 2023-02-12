# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.


# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1

from collections import Counter
from typing import List


def single_number(nums: List[int]) -> bool:

    freq = Counter(nums)
    freq_sort = dict(sorted(freq.items(), key=lambda item: item[1]))

    return freq_sort.keys()[0]
