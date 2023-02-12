# Given a binary tree, determine if it is
# height-balanced

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:


# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true

# https://leetcode.com/problems/balanced-binary-tree/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    if abs(get_height(root.left) - get_height(root.right)) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)


def get_height(root: Optional[TreeNode]) -> int:

    if not root:
        return 0

    return max(get_height(root.left), get_height(root.right)) + 1
