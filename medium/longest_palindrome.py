# You are given an array of strings words. Each element of words consists of two lowercase English letters.

# Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

# Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

# A palindrome is a string that reads the same forward and backward.


# Example 1:
# Input: words = ["lc","cl","gg"]
# Output: 6
# Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
# Note that "clgglc" is another longest palindrome that can be created.

# Example 2:
# Input: words = ["ab","ty","yt","lc","cl","ab"]
# Output: 8
# Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
# Note that "lcyttycl" is another longest palindrome that can be created.

# Example 3:
# Input: words = ["cc","ll","xx"]
# Output: 2
# Explanation: One longest palindrome is "cc", of length 2.
# Note that "ll" is another longest palindrome that can be created, and so is "xx".

# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description/

from typing import List


def longestPalindrome(words: List[str]) -> int:

    # Initialize a dictionary to keep track of the frequency of each word
    d = {}
    # Initialize a variable to keep track of the maximum length of the palindrome
    max_len = 0
    # Initialize a variable to keep track of whether there is a central letter in the palindrome
    central = False

    # Iterate through each word in the list of words
    for word in words:
        # If the word is not already in the dictionary, add it with a frequency of 1
        if word not in d:
            d[word] = 1
        # If the word is already in the dictionary, increment its frequency by 1
        else:
            d[word] += 1

    # Define a helper function to check whether a word is a palindrome
    def ispalindrome(word):
        if word == word[::-1]:
            return True
        return False

    # Iterate through each word and its frequency in the dictionary
    for word, count_word in d.items():

        # If the word is a palindrome
        if ispalindrome(word):
            # If the frequency of the word is even, add 2 times the frequency to the maximum length
            if count_word % 2 == 0:
                max_len += 2 * count_word
            # If the frequency of the word is odd, add 2 times (frequency - 1) to the maximum length and set central to True
            else:
                max_len += 2 * (count_word - 1)
                central = True

        # If the word is not a palindrome, but its reverse is in the dictionary
        else:
            if word in d and word[::-1] in d:
                # Add 2 times the minimum frequency of the word and its reverse to the maximum length
                max_len += 2 * min(d[word], d[word[::-1]])

    # If there is a central letter in the palindrome, add 2 to the maximum length
    if central:
        max_len += 2

    # Return the maximum length of the palindrome
    return max_len
