# You have n bulbs in a row numbered from 1 to n. Initially, all the bulbs are turned off. We turn on exactly one bulb every day until all bulbs are on after n days.

# You are given an array bulbs of length n where bulbs[i] = x means that on the (i+1)th day, we will turn on the bulb at position x where i is 0-indexed and x is 1-indexed.

# Given an integer k, return the minimum day number such that there exists two turned on bulbs that have exactly k bulbs between them that are all turned off. If there isn't such day, return -1.

# Example 1:

# Input: bulbs = [1,3,2], k = 1
# Output: 2
# Explanation:
# On the first day: bulbs[0] = 1, first bulb is turned on: [1,0,0]
# On the second day: bulbs[1] = 3, third bulb is turned on: [1,0,1]
# On the third day: bulbs[2] = 2, second bulb is turned on: [1,1,1]
# We return 2 because on the second day, there were two on bulbs with one off bulb between them.

# Example 2:

# Input: bulbs = [1,2,3], k = 1
# Output: -1
from typing import List


def k_empty_slots(bulbs: List[int], k: int) -> int:
    days = [0] * len(bulbs)
    for i, bulb in enumerate(bulbs):
        days[bulb - 1] = i + 1
    left, right = 0, k + 1
    res = float("inf")
    while right < len(days):
        for i in range(left + 1, right):
            if days[i] < days[left] or days[i] < days[right]:
                left, right = i, i + k + 1
                break
        else:
            res = min(res, max(days[left], days[right]))
            left, right = right, right + k + 1
    return res if res < float("inf") else -1


list = [1, 3, 2]
k = 1

print(k_empty_slots(list, k))
