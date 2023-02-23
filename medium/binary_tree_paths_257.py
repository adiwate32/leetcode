# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.

# Example 1:
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]

# Example 2:
# Input: root = [1]
# Output: ["1"]

# https://leetcode.com/problems/binary-tree-paths/description/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        if not root:
            return []

        res = []

        def paths(root, path):

            if not any([root.left, root.right]):
                res.append(path)

            paths(root.left, path + "->" + str(root.left.val)) if root.left else None
            paths(root.right, path + "->" + str(root.right.val)) if root.right else None

        paths(root, str(root.val))
        return res
