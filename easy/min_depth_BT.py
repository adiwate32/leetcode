# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.


# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# Example 2:

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root: Optional[TreeNode]) -> int:

    if not root:
        return 0

    if not root.left:
        return 1 + min_depth(root.right)

    if not root.right:
        return 1 + min_depth(root.left)

    return 1 + min(min_depth(root.right), min_depth(root.left))
