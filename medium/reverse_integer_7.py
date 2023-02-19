# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# https://leetcode.com/problems/reverse-integer/description/


class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1

        num = abs(x)

        rev = 0

        while num > 0:
            rem = num % 10

            rev = rev * 10 + rem
            num = num // 10

            if rev >= 2**31 - 1:
                return 0

        return sign * rev
