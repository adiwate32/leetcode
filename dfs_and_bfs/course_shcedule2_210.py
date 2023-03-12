# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

# Example 1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

# Example 2:
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

# https://leetcode.com/problems/course-schedule-ii/description/
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create a map of courses and their prerequisites
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        stack = []
        visited, cycle = set(), set()
        # define the dfs function
        def dfs(crs):
            # if a cycle is detected, return False
            if crs in cycle:
                return False
            # if the node has already been visited, return True
            if crs in visited:
                return True
            # mark the node as part of the cycle and explore its prerequisites
            cycle.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            # remove the node from the cycle and mark it as visited
            cycle.remove(crs)
            visited.add(crs)
            # add the course to the topological sort order
            stack.append(crs)
            return True

        # iterate through each course and explore its prerequisites
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        # if a valid order is found, return it
        return stack
