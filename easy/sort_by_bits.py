# You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

# Return the array after sorting it.


# Example 1:

# Input: arr = [0,1,2,3,4,5,6,7,8]
# Output: [0,1,2,4,8,3,5,6,7]
# Explantion: [0] is the only integer with 0 bits.
# [1,2,4,8] all have 1 bit.
# [3,5,6] have 2 bits.
# [7] has 3 bits.
# The sorted array by bits is [0,1,2,4,8,3,5,6,7]
# Example 2:

# Input: arr = [1024,512,256,128,64,32,16,8,4,2,1]
# Output: [1,2,4,8,16,32,64,128,256,512,1024]
# Explantion: All integers have 1 bit in the binary representation, you should just sort them in ascending order.

# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/

from typing import List


def sortByBits1(arr: List[int]) -> List[int]:

    arr = sorted(arr)

    bits_map = {}
    if not arr:
        return arr

    for i in arr:

        temp = i
        cnt = 0
        while temp > 0:

            if temp % 2 != 0:
                cnt += 1
            temp = temp // 2

        if cnt not in bits_map:
            bits_map[cnt] = [i]
        else:
            bits_map[cnt].append(i)

    sort_bits_map = dict(sorted(bits_map.items(), key=lambda x: x[0]))

    res = []
    for val in sort_bits_map.values():
        res.extend(val)

    return res


def sortByBits2(arr: List[int]) -> List[int]:

    return sorted(sorted(arr), key=lambda x: bin(x).count("1"))
