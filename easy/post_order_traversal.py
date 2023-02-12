# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [3,2,1]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]

# https://leetcode.com/problems/binary-tree-postorder-traversal/description/


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def post_order_traversal(root: Optional[TreeNode]) -> List[int]:

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
