# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# https://leetcode.com/problems/permutation-in-string/description/

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Get the length of the window to search for
        window = len(s1)

        # Get the frequency count of the characters in s1
        c1 = Counter(s1)

        # Iterate through all possible substrings of s2 of length window and check if their frequency count is equal to that of s1
        for i in range(len(s2) - window + 1):
            c2 = Counter(s2[i : i + window])
            if c1 == c2:
                return True

        # If no substring is found, return False
        return False
