"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        if not root:
            return res

        def dfs(node, path):
            if not any([node.left, node.right]):
                res.append(path)

            if node.left:
                dfs(node.left, path + "->" + str(node.left.val))
            else:
                None

            if node.right:
                dfs(node.right, path + "->" + str(node.right.val))
            else:
                None

        dfs(root, str(root.val))
        return res
