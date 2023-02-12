# Given a string s, return the length of the longest
# substring
#  that contains at most two distinct characters.


# Example 1:

# Input: s = "eceba"
# Output: 3
# Explanation: The substring is "ece" which its length is 3.
# Example 2:

# Input: s = "ccaabbb"
# Output: 5
# Explanation: The substring is "aabbb" which its length is 5.

# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/


def lengthOfLongestSubstringTwoDistinct(s: str) -> int:

    max_len = 0
    start = 0
    end = 0
    d = {}

    while end < len(s):
        d[s[end]] = end
        if len(d) > 2:
            min_ind = min(d.values())
            start = min_ind + 1
            del d[s[min_ind]]

        max_len = max(max_len, end - start + 1)
        end += 1

    return max_len
