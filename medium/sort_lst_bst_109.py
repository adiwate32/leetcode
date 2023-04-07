"""
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.

Example 1:
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

Example 2:
Input: head = []
Output: []
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        mid_ele = self.middle_ele(head)

        mid_node = TreeNode(mid_ele.val)

        if head == mid_ele:
            return mid_node

        mid_node.left = self.sortedListToBST(head)
        mid_node.right = self.sortedListToBST(mid_ele.next)

        return mid_node

    def middle_ele(self, head):
        prev = None
        slow, fast = head, head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if prev:
            prev.next = None

        return slow
