"""
    Given a string s, find the length of the longest 
    substring
    without repeating characters.

    Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

    https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""

from collections import Counter


# two pointer
def length_of_sub_string(s: str) -> int:
    cntr = Counter()

    left = right = 0

    ans = 0
    while right < len(s):
        r = s[right]
        cntr[r] += 1

        while cntr[r] > 1:
            l = s[left]
            cntr[l] -= 1
            left += 1

        ans = max(ans, right - left + 1)
        right += 1

    return ans


# sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        i = 0
        max_c = 0

        for j in range(len(s)):
            if s[j] in d:
                i = max(d[s[j]], i)

            max_c = max(max_c, j - i + 1)
            d[s[j]] = j + 1

        return max_c
