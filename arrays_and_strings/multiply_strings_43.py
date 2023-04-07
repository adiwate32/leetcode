"""
    Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

    Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.


    Example 1:
    Input: num1 = "2", num2 = "3"
    Output: "6"

    Example 2:
    Input: num1 = "123", num2 = "456"
    Output: "56088"

    https://leetcode.com/problems/multiply-strings/description/?envType=study-plan&id=level-2
"""


def multiply(num1: str, num2: str) -> str:
    # If either of the inputs is "0", return "0"
    if num1 == "0" or num2 == "0":
        return "0"

    # Reverse the strings to make them easier to work with
    nums1 = num1[::-1]
    nums2 = num2[::-1]

    # Create a list with the length of the sum of the lengths of both inputs
    # filled with 0's to store the intermediate results
    res = [0] * (len(nums1) + len(nums2))

    # Loop through each digit in the first number
    for i1 in range(len(nums1)):
        # Loop through each digit in the second number
        for i2 in range(len(nums2)):
            # Multiply the digits and add them to the intermediate results list
            digit = int(nums1[i1]) * int(nums2[i2])
            res[i1 + i2] += digit

            # Take care of carry over
            res[i1 + i2 + 1] += res[i1 + i2] // 10
            res[i1 + i2] = res[i1 + i2] % 10

    # Remove any trailing 0's from the intermediate results list
    while not res[-1]:
        res.pop()

    # Convert the intermediate results list to strings and reverse it back
    res_map = list(map(str, res))
    return "".join(res_map[::-1])
