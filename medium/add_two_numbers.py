# Definition for singly-linked list.

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# https://leetcode.com/problems/add-two-numbers/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:

    carry = 0

    dummy_head = ListNode(0)
    curr = dummy_head

    while l1 or l2 or carry:

        if l1:
            l1val = l1.val
            l1 = l1.next
        else:
            l1val = 0

        if l2:
            l2val = l2.val
            l2 = l2.next
        else:
            l2val = 0

        column_sum = carry + l1val + l2val

        new_node = ListNode(column_sum % 10)

        carry = column_sum // 10

        curr.next = new_node

        curr = new_node

    return dummy_head.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print(add_two_numbers(l1, l2).val)
