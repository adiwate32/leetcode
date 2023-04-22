"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []

        def preorder(root):
            if not root:
                return

            st.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return st


# iterative preorder traversal
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]

        res = []

        while stack:
            node = stack.pop()

            if node:
                res.append(node.val)

                if node.left:
                    stack.append(node.left)

                if node.right:
                    stack.append(node.right)

        return res
