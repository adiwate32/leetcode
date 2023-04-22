"""
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

Example 1:
Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

Example 2:
Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
"""


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        rows = len(str1)
        cols = len(str2)

        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                if str1[r - 1] == str2[c - 1]:
                    dp[r][c] = 1 + dp[r - 1][c - 1]
                else:
                    dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])

        i, j = rows, cols
        res = ""

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                res += str1[i - 1]
                i -= 1
                j -= 1

            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    res += str1[i - 1]
                    i -= 1
                else:
                    res += str2[j - 1]
                    j -= 1

        while i > 0:
            res += str1[i - 1]
            i -= 1

        while j > 0:
            res += str2[j - 1]
            j -= 1

        return res[::-1]
