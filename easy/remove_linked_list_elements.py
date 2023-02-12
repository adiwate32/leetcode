# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

# Example 2:
# Input: head = [], val = 1
# Output: []
# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []

# https://leetcode.com/problems/remove-linked-list-elements/solutions/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:

    while head and head.val == val:
        head = head.next

    temp = head

    while temp:
        while temp and temp.next and temp.next.val == val:

            temp.next = temp.next.next
        temp = temp.next

    return head
