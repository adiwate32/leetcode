# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# https://leetcode.com/problems/longest-consecutive-sequence/description/

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # If the input list is empty, there is no consecutive sequence, so return 0
        if not nums:
            return 0

        # Sort the list of numbers
        nums.sort()
        long_streak = 1
        curr_streak = 1

        # Iterate through the sorted list of numbers and calculate the length of the longest consecutive sequence
        for i in range(1, len(nums)):

            # If the current number is one greater than the previous number, increase the current streak by 1
            if nums[i] == nums[i - 1] + 1:
                curr_streak += 1
            # If the current number is not one greater than the previous number, reset the current streak to 1
            else:
                curr_streak = 1

            # Update the length of the longest consecutive sequence if the current streak is longer than the longest streak
            long_streak = max(long_streak, curr_streak)

        # Return the length of the longest consecutive sequence
        return long_streak
