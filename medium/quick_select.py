# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# You must solve it in O(n) time complexity.


# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

from typing import List


def findKthLargest(nums: List[int], k: int) -> int:

    k = len(nums) - k

    def quick_select(l, r):

        pivot, p = nums[r], l

        for i in range(l, r):

            if nums[i] <= pivot:

                nums[p], nums[i] = nums[i], nums[p]
                p += 1

        nums[p], nums[r] = nums[r], nums[p]

        if p > k:

            return quick_select(0, p - 1)

        elif p < k:

            return quick_select(p + 1, r)

        else:
            return nums[p]

    return quick_select(0, len(nums) - 1)
