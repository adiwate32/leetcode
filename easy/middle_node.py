# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# https://leetcode.com/problems/middle-of-the-linked-list/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:

    # If the head is None, return None
    if not head:
        return

    # Initialize two pointers, slow and fast, to point to the head of the list
    slow = fast = head

    # While the fast pointer and the node after it are not None, increment the slow pointer by one and the fast pointer by two
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # When the loop terminates, the slow pointer will point to the middle node of the list
    return slow
