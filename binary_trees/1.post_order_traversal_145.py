"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []

        def postOrder(root):
            if not root:
                return

            postOrder(root.left)
            postOrder(root.right)
            st.append(root.val)

        postOrder(root)

        return st


# iterative
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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

        return res[::-1]
