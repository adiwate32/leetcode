"""
    Given the root of a binary tree and a node u in the tree, return the nearest node on the same level that is to the right of u, or return null if u is the rightmost node in its level.

    Example 1:
    Input: root = [1,2,3,null,4,5,6], u = 4
    Output: 5
    Explanation: The nearest node on the same level to the right of node 4 is node 5.

    Example 2:
    Input: root = [3,null,4,2], u = 2
    Output: null
    Explanation: There are no nodes to the right of 2.

    https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/description/
"""


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        if root is None:
            return None
        next_q = [root]

        while next_q:
            curr_q = next_q
            next_q = []

            while curr_q:
                node = curr_q.pop(0)

                if node == u:
                    return curr_q.pop(0) if curr_q else None

                if node.left:
                    next_q.append(node.left)

                if node.right:
                    next_q.append(node.right)
