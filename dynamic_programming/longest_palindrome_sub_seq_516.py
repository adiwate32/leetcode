"""
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
"""


class Solution:
    def longestPalindromeSubseq(self, text1: str) -> int:

        text2 = text1[::-1]

        rows = len(text1)
        cols = len(text2)

        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                if text1[r - 1] == text2[c - 1]:
                    dp[r][c] = 1 + dp[r - 1][c - 1]
                else:
                    dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])

        return dp[rows][cols]
