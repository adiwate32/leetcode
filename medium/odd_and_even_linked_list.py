# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]

# Example 2:
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]

# https://leetcode.com/problems/odd-even-linked-list/description/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:

    # Check if the input is None
    if not head:
        return None

    # Initialize two pointers: odd and even
    odd = head
    even = head.next

    # Save the head of the even-indexed list
    even_head = even

    # Traverse the linked list
    while even and even.next:

        # Link the next odd-indexed node to the current even-indexed node
        odd.next = even.next

        # Move the odd pointer to the next odd-indexed node
        odd = odd.next

        # Link the next even-indexed node to the current odd-indexed node
        even.next = odd.next

        # Move the even pointer to the next even-indexed node
        even = even.next

    # Link the end of the odd-indexed list to the head of the even-indexed list
    odd.next = even_head

    # Return the head of the reordered linked list
    return head
