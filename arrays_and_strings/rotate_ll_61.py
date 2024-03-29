"""
    Given the head of a linked list, rotate the list to the right by k places.

    Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [4,5,1,2,3]

    Example 2:
    Input: head = [0,1,2], k = 4
    Output: [2,0,1]  

    https://leetcode.com/problems/rotate-list/description/
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return

        if not head.next:
            return head
        tail = head
        n = 1

        while tail.next:
            tail = tail.next
            n += 1

        tail.next = head

        new_tail = head
        for _ in range(n - k % n - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head
