from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        palindrome_arr = []

        cur = head
        while cur is not None:
            palindrome_arr.append(cur.val)
            cur = cur.next
        
        i, j = 0, len(palindrome_arr) - 1
        while i < j:
            if palindrome_arr[i] == palindrome_arr[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
    
    '''
    singly linked list -> can not traverse backwards through the list
    idea #1: traverse through the list and store values in array then check if array is palindrome
        - O(n) time but O(n) space
    '''