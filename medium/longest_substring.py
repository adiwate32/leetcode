# Given a string s, find the length of the longest
# substring
#  without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

from collections import Counter


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


print(length_of_sub_string("abcabcbb"))
