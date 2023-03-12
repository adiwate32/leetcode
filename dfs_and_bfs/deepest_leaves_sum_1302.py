"""
Given the root of a binary tree, return the sum of values of its deepest leaves.
 
Example 1:
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Example 2:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19

https://leetcode.com/problems/deepest-leaves-sum/description/
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        deepest_sum = depth = 0

        stack = [(root, 0)]

        while stack:
            node, curr_depth = stack.pop()

            if not node.left and not node.right:
                if depth < curr_depth:
                    deepest_sum = node.val
                    depth = curr_depth

                elif depth == curr_depth:
                    deepest_sum += node.val
            else:
                if node.left:
                    stack.append((node.left, curr_depth + 1))

                if node.right:
                    stack.append((node.right, curr_depth + 1))

        return deepest_sum
