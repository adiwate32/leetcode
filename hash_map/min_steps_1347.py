"""
    You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.
    Return the minimum number of steps to make t an anagram of s.
    An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

    Example 1:
    Input: s = "bab", t = "aba"
    Output: 1
    Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

    Example 2:
    Input: s = "leetcode", t = "practice"
    Output: 5
    Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

    Example 3:
    Input: s = "anagram", t = "mangaar"
    Output: 0
    Explanation: "anagram" and "mangaar" are anagrams. 
"""
from collections import defaultdict


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hash_map = defaultdict(int)
        for i in range(len(s)):
            hash_map[s[i]] += 1
            hash_map[t[i]] -= 1
        return sum(abs(i) for i in hash_map.values()) // 2
