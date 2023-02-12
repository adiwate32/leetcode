# Given two binary strings a and b, return their sum as a binary string.


# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

# https://leetcode.com/problems/add-binary/description/


def add_binary(a: str, b: str) -> str:

    ans_stack = []
    carry = 0
    lst_a = list(a)
    lst_b = list(b)

    while lst_a or lst_b or carry:

        a_val = int(lst_a.pop()) if lst_a else 0
        b_val = int(lst_b.pop()) if lst_b else 0

        sum = a_val + b_val + carry

        new_ele = sum % 2

        carry = sum // 2

        ans_stack.insert(0, str(new_ele))

    return "".join(ans_stack)
