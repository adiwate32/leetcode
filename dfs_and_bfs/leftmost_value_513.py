"""
    Given the root of a binary tree, return the leftmost value in the last row of the tree.

    Example 1:
    Input: root = [2,1,3]
    Output: 1

    Example 2:
    Input: root = [1,2,3,4,null,5,6,null,null,7]
    Output: 7

    https://leetcode.com/problems/find-bottom-left-tree-value/description/
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node, currdepth, depth, left):
            if not node:
                return depth, left

            if depth < currdepth:
                depth = currdepth
                left = node.val

            if node.left:
                depth, left = dfs(node.left, currdepth + 1, depth, left)

            if node.right:
                depth, left = dfs(node.right, currdepth + 1, depth, left)

            return depth, left

        depth, left = dfs(root, 0, -1, -1)
        return left


from collections import deque


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        q = deque([root])
        leftmost = root.val

        while q:
            size = len(q)
            leftmost = q[0].val
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return leftmost
