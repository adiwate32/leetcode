# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# https://leetcode.com/problems/majority-element/description/

from collections import Counter
from typing import List


def majority_element(nums: List[int]) -> int:
    cntr = Counter()

    for i in nums:
        cntr[i] += 1

    return sorted(cntr, key=cntr.get, reverse=True)[0]
