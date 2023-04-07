# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

# Example 1:
# Input: root = [4,2,6,1,3]
# Output: 1

# Example 2:
# Input: root = [1,0,48,null,null,12,49]
# Output: 1

# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min = float("inf")
        self.prev = None

        def dfs(root):
            if root.left:
                dfs(root.left)
            if self.prev:
                self.min = min(self.min, root.val - self.prev)
            self.prev = root.val

            if root.right:
                dfs(root.right)

        dfs(root)

        return self.min
