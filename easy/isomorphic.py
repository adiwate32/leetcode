# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true

# https://leetcode.com/problems/isomorphic-strings/description/


def transform_string(s: str) -> str:
    index_mapping = {}
    new_str = []

    for index, char in enumerate(s):
        if char not in index_mapping:
            index_mapping[char] = index

        new_str.append(str(index_mapping[char]))

    return ",".join(new_str)


def is_isomophic(s: str, t: str) -> bool:
    return transform_string(s) == transform_string(t)


print(is_isomophic("foo", "bar"))
