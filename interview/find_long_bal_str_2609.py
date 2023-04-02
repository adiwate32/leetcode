"""
    You are given a binary string s consisting only of zeroes and ones.
    A substring of s is considered balanced if all zeroes are before ones and the number of zeroes is equal to the number of ones inside the substring. Notice that the empty substring is considered a balanced substring.

    Return the length of the longest balanced substring of s.

    A substring is a contiguous sequence of characters within a string.

    Example 1:
    Input: s = "01000111"
    Output: 6
    Explanation: The longest balanced substring is "000111", which has length 6.

    Example 2:
    Input: s = "00111"
    Output: 4
    Explanation: The longest balanced substring is "0011", which has length 4. 

    Example 3:
    Input: s = "111"
    Output: 0
    Explanation: There is no balanced substring except the empty substring, so the answer is 0.
"""


class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:

        max_ans = 0
        zero_cnt = 0
        one_cnt = 0
        n = len(s)

        for i in range(n):
            if s[i] == "0":
                if zero_cnt == one_cnt:
                    max_ans = max(max_ans, one_cnt)
                zero_cnt += 1
                one_cnt = 0
            else:
                one_cnt += 1
                if one_cnt <= zero_cnt:
                    max_ans = max(max_ans, one_cnt)
                if i + 1 < n and s[i] != s[i + 1]:
                    zero_cnt = 0

        return 2 * max_ans
