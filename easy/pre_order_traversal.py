# Given the root of a binary tree, return the preorder traversal of its nodes' values.


# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,2,3]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pre_order_traversal(root: Optional[TreeNode]) -> List[int]:

    stack = [root]

    res = []

    while stack:

        node = stack.pop()
        if node:

            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)

    return res
