# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.


# Example 1:

# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:

# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation:
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

# https://leetcode.com/problems/degree-of-an-array/description/

from typing import List


def find_shortest_sub_array(nums: List[int]) -> int:
    idx_map = {}
    for i, num in enumerate(nums):
        if num in idx_map:
            idx_map[num].append(i)
        else:
            idx_map[num] = [i]

    max_ele = max([len(i) for i in idx_map.values()])

    return min([i[-1] - i[0] for i in idx_map.values() if len(i) == max_ele]) + 1
