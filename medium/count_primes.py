# Given an integer n, return the number of prime numbers that are strictly less than n.


# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0

# https://leetcode.com/problems/count-primes/description/


def count_primes(n: int) -> int:

    count = 0

    seen_num = [0] * n

    for num in range(2, n):

        if seen_num[num]:
            continue

        count += 1

        seen_num[num * num : n : num] = [1] * ((n - 1) // num - num + 1)

    return count


print(count_primes(1987654))
