"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        q1 = []
        q2 = []
        for i in range(len(s)):
            if s[i] != "#":
                q1.append(s[i])
            elif q1:
                q1.pop()

        for i in range(len(t)):
            if t[i] != "#":
                q2.append(t[i])
            elif q2:
                q2.pop()

        if q1 != q2:
            return False

        return True
