# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=study-plan&id=level-2

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:

    i = 0

    # Create a new ListNode and set its next node to the head of the linked list.
    dummy = ListNode(0)
    dummy.next = head

    # Create two pointers, both initially pointing to the dummy node.
    first = dummy
    second = dummy

    # Move the second pointer n nodes ahead of the first pointer.
    while i <= n:
        second = second.next
        i += 1

    # Move both pointers simultaneously until the second pointer reaches the end of the list.
    while second:
        first = first.next
        second = second.next

    # Remove the nth node by skipping over it.
    first.next = first.next.next

    # Return the new head of the linked list.
    return dummy.next
