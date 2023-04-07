# Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

# Example 1:
# Input: root = [4,2,6,1,3]
# Output: 1

# Example 2:
# Input: root = [1,0,48,null,null,12,49]
# Output: 1

# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        bst_lst = []

        def inoder_traversal(root):
            if root:
                if root.left:
                    inoder_traversal(root.left)
                bst_lst.append(root.val)
                if root.right:
                    inoder_traversal(root.right)

        inoder_traversal(root)

        diff = float("inf")

        for i in range(len(bst_lst) - 1):
            if bst_lst[i + 1] - bst_lst[i] < diff:
                diff = bst_lst[i + 1] - bst_lst[i]

        return int(diff)
