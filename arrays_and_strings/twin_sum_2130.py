"""
    In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

    For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
    The twin sum is defined as the sum of a node and its twin.

    Given the head of a linked list with even length, return the maximum twin sum of the linked list.

    Example 1:
    Input: head = [5,4,2,1]
    Output: 6
    Explanation:
    Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
    There are no other nodes with twins in the linked list.
    Thus, the maximum twin sum of the linked list is 6. 

    Example 2:
    Input: head = [4,2,2,3]
    Output: 7
    Explanation:
    The nodes with twins present in this linked list are:
    - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
    - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
    Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        max_val = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr, prev = slow, None

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        while prev:
            max_val = max(max_val, head.val + prev.val)
            head = head.next
            prev = prev.next

        return max_val
