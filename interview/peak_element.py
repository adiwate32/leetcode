"""
    You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

    You must write an algorithm that runs in O(log n) time.

    Example 1:
    Input: nums = [1,2,3,1]
    Output: 2
    Explanation: 3 is a peak element and your function should return the index number 2.

    Example 2:
    Input: nums = [1,2,1,3,5,6,4]
    Output: 5
    Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        for i in range(n):
            if 0 < i < n - 1 and nums[i - 1] < nums[i] > nums[i + 1]:
                return i
            elif i == 0 and nums[i] > nums[i + 1]:
                return i
            elif i == n - 1 and nums[i - 1] < nums[i]:
                return i
