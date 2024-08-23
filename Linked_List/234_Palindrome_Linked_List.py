from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        start, end = head, None

        # Find the midpoint using fast/slow pointers 
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        midpoint = slow.next

        # Reverse the latter half of the linked list
        prev, cur = None, midpoint
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        end = prev    # cur is None so prev is end of the list

        # Compare the start of the list and the end of the list to check if the list is a palindrome
        while start is not None and end is not None:
            if start.val != end.val:
                return False
            start, end = start.next, end.next
        return True
                   
    '''
    singly linked list -> can not traverse backwards through the list
    idea #1: traverse through the list and store values in array then check if array is palindrome
        - O(n) time but O(n) space
    idea #2: find the midpoint using fast/slow pointers then reverse the latter half of the linked list
        - O(n) time and O(1) space
    '''