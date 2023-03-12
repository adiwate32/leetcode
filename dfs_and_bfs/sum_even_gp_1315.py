"""
    Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

    A grandparent of a node is the parent of its parent if it exists.

    Example 1:
    Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
    Output: 18
    Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.

    Example 2:
    Input: root = [1]
    Output: 0

    https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        sumval = 0

        def dfs(node, p, gp):
            if not node:
                return
            nonlocal sumval

            if gp and gp.val % 2 == 0:
                sumval += node.val

            dfs(node.left, node, p)
            dfs(node.right, node, p)

        dfs(root, None, None)
        return sumval
