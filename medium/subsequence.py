# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

# https://leetcode.com/problems/is-subsequence/description/


def isSubsequence(s: str, t: str) -> bool:
    source_len = len(s)
    target_len = len(t)

    if len(s) == 0:
        return True

    dp = [[0] * (target_len + 1) for _ in range(source_len + 1)]

    for col in range(1, target_len + 1):
        for row in range(1, source_len + 1):
            if s[row - 1] == t[col - 1]:
                dp[row][col] = dp[row - 1][col - 1] + 1

            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

            if dp[row][col] == len(s):
                return True

    return False
