# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# https://leetcode.com/problems/longest-common-prefix/

from typing import List


def longest_common_prefix_1(strs: List[str]) -> str:
    strs.sort()
    first, last = strs[0], strs[-1]

    index = 0
    while index < len(first) and index < len(last):
        if first[index] != last[index]:
            break

        index += 1

    return first[:index]


def longest_common_prefix_2(strs: List[str]) -> str:
    if not strs:
        return ""

    prefix = min(strs, key=len)
    for i in range(len(prefix)):
        for string in strs:
            if i >= len(prefix) or string[i] != prefix[i]:
                return prefix[:i]

        return prefix
