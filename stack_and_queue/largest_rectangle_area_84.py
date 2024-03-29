"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [None] * n
        right = [None] * n
        st = []

        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()

            if not st:
                left[i] = 0

            else:
                left[i] = st[-1] + 1

            st.append(i)

        st = []

        for i in range(n - 1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()

            if not st:
                right[i] = n - 1

            else:
                right[i] = st[-1] - 1

            st.append(i)

        area = 0
        for i in range(n):
            area = max(area, (right[i] - left[i] + 1) * heights[i])

        return area
