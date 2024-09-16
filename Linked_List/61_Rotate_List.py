from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # count the number of nodes in the list -> O(n)
        cur = head
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        
        # return if list is empty
        if count == 0:
            return head
        
        # calculate the number of rotations to make and the index of the new head -> O(1)
        nofrotations = k % count
        new_head_idx = count - nofrotations
        # return the original list if number of rotations is 0
        if nofrotations == 0:
            return head
        
        cur = head
        idx = 0
        # the node before the new head is the new tail (points to None) -> O(n)
        while idx < new_head_idx - 1:
            cur = cur.next
            idx += 1
        new_tail = cur
        new_head = cur.next
        new_tail.next = None
        
        # let the tail of the original list point to the old head -> O(n)
        cur = new_head
        while cur.next is not None:
            cur = cur.next
        temp_tail = cur
        temp_tail.next = head

        return new_head
    
    '''
    given the head, rotate the list to the right by k

    count the # of nodes in the list -> O(n)
    suppose that the list is 0-indexed:
        - if k = 1 then the head is at index 1
        - if k = n then the head is at index n
        - thus the head must be at index k % n
    so if the head is at index m where m < n then there are m nodes before the head
        - the last m nodes of the list start at index n - m
            - let this node be the beginning of the list
    '''