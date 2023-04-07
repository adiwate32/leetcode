# Given the head of a singly linked list, return true if it is a
# palindrome
#  or false otherwise.


# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false

# https://leetcode.com/problems/palindrome-linked-list/description/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: Optional[ListNode]) -> bool:
    # Set a temporary variable to the head of the linked list.
    temp = head

    # Initialize an empty array to hold the values from the linked list.
    arr = []

    # Traverse the linked list and add each value to the array.
    while temp:
        arr.append(temp.val)
        temp = temp.next

    # Set two pointers at the beginning and end of the array.
    left, right = 0, len(arr) - 1

    # Iterate over the array, comparing values at the two pointers.
    for i in range(len(arr)):
        # While the left pointer is less than or equal to the right pointer...
        while left <= right:
            # If the values at the left and right pointers don't match, the list is not a palindrome.
            if arr[left] != arr[right]:
                return False

            # Move the pointers inwards.
            left += 1
            right -= 1

    # If all values have been compared and matched, the list is a palindrome.
    return True
