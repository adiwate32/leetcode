# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Example 2:
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Get the length of the window to search for
        window = len(p)

        # If the window size is greater than the length of s, there can be no anagrams of p in s
        if window > len(s):
            return []

        # Get the frequency count of the characters in p
        c1 = Counter(p)

        # Iterate through all possible substrings of s of length window and check if their frequency count is equal to that of p
        res = []
        for i in range(len(s) - window + 1):
            c2 = Counter(s[i : i + window])
            if c1 == c2:
                res.append(i)

        # Return the list of starting indices of all substrings that are anagrams of p
        return res
