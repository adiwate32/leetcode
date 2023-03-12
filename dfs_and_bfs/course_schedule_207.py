"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""

from typing import List

from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        pre_map = defaultdict(list)
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        def dfs(crs, pre_map, visited, cycle):

            if crs in cycle:
                return False

            if crs in visited:
                return True

            cycle.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre, pre_map, visited, cycle):
                    return False
            cycle.remove(crs)
            visited.add(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs, pre_map, set(), set()):
                return False

        return True
