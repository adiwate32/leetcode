"""
    Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

    Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

    Example 1:
    Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
    Output: 1

    Example 2:
    Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
    Output: 3
"""
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hash_map = {}
        cn = 0

        for d in dominoes:
            big = max(d[0], d[1])
            small = min(d[0], d[1])

            key = big * 10 + small

            if key in hash_map:
                cn += hash_map[key]
                hash_map[key] += 1
            else:
                hash_map[key] = 1

        return cn
