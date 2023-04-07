# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.


# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false


def word_pattern(pattern: str, s: str) -> bool:
    index_mapping = {}

    words = s.split(" ")

    if len(words) != len(pattern):
        return False

    for i in range(len(words)):
        p = pattern[i]
        w = words[i]

        char_key = "char_{}".format(p)
        char_word = "word_{}".format(w)

        if char_key not in index_mapping:
            index_mapping[char_key] = i

        if char_word not in index_mapping:
            index_mapping[char_word] = i

        if index_mapping[char_key] != index_mapping[char_word]:
            return False

    return True
