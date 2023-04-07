"""
    Given an array of integer arrays arrays where each arrays[i] is sorted in strictly increasing order, return an integer array representing the longest common subsequence between all the arrays.

    A subsequence is a sequence that can be derived from another sequence by deleting some elements (possibly none) without changing the order of the remaining elements.

    Example 1:
    Input: arrays = [[1,3,4],
                    [1,4,7,9]]
    Output: [1,4]
    Explanation: The longest common subsequence in the two arrays is [1,4].

    Example 2:
    Input: arrays = [[2,3,6,8],
                    [1,2,3,5,6,7,10],
                    [2,3,4,6,9]]
    Output: [2,3,6]
    Explanation: The longest common subsequence in all three arrays is [2,3,6].

    Example 3:
    Input: arrays = [[1,2,3,4,5],
                    [6,7,8]]
    Output: []
    Explanation: There is no common subsequence between the two arrays.

    https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/description/
"""
from typing import List
from collections import defaultdict


class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        hash_map = defaultdict(int)
        n = len(arrays)

        res = []
        for array in arrays:
            for a in array:
                hash_map[a] += 1
                if hash_map[a] == n:
                    res.append(a)

        return res
