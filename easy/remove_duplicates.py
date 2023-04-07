# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.


# Example 1:


# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/


# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr:
            while curr and curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next

            curr = curr.next

        return head
