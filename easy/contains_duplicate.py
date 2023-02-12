# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
from collections import Counter
from typing import List


def contains_duplicate(nums: List[int]) -> bool:

    freq = Counter(nums)
    freq_values = list(freq.values())
    freq_values.sort()

    for i in freq_values:
        if i > 1:
            return True

    return False


print(contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
