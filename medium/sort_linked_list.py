# Given the head of a linked list, return the list after sorting it in ascending order.

# Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# Example 2:
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]

# Example 3:
# Input: head = []
# Output: []

# https://leetcode.com/problems/sort-list/description/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # check if the list is empty or has only one element
        if not head or not head.next:
            return head

        # get the middle element of the list
        right = self.get_middle_ele(head)

        # split the list into two halves
        tmp = right.next
        right.next = None
        right = tmp

        # recursively sort the two halves
        left = self.sortList(head)
        right = self.sortList(right)

        # merge the two sorted halves
        return self.merge(left, right)

    def get_middle_ele(self, head):
        # initialize two pointers, one moving at twice the speed of the other
        slow = head
        fast = head.next

        # while the fast pointer hasn't reached the end of the list
        while fast and fast.next:
            # move the slow pointer one step
            slow = slow.next
            # move the fast pointer two steps
            fast = fast.next.next

        # return the slow pointer, which is now at the middle element of the list
        return slow

    def merge(self, left, right):
        # create a new linked list to store the merged elements
        new_node = tail = ListNode(0)

        # while both left and right lists have elements
        while left and right:
            # compare the values of the two elements, and add the smaller one to the merged list
            if left.val >= right.val:
                tail.next = right
                right = right.next
            else:
                tail.next = left
                left = left.next

            # move the tail pointer to the end of the merged list
            tail = tail.next

        # add any remaining elements from the left list to the merged list
        if left:
            tail.next = left

        # add any remaining elements from the right list to the merged list
        if right:
            tail.next = right

        # return the merged list
        return new_node.next
