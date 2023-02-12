# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1

# https://leetcode.com/problems/first-unique-character-in-a-string/description/


def firstUniqChar(s: str) -> int:

    index_map = {}

    for i, char in enumerate(s):

        if char not in index_map:
            index_map[char] = 1
        else:
            index_map[char] += 1

    index = -1
    for i in range(len(s)):
        if index_map[s[i]] == 1:
            index = i
            break

    return index
