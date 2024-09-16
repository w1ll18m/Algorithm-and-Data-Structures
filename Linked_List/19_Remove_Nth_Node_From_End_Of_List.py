from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_a, a = dummy, head
        idx_b, b = 1, head

        # find the node at index n
        while idx_b != n:
            b = b.next
            idx_b += 1

        # iterate b until we reach the last node, a should point at the node at index m - n + 1
        while b.next is not None:
            b = b.next
            prev_a = a
            a = a.next
        
        # remove the node at index m - n + 1
        prev_a.next = a.next
        
        return dummy.next
 
    '''
    given the head, remove the nth node from the end of the list
    let the list be 1-indexed and be length m then:
        - the nth node from the end of the list has index m - n + 1
        - so let b = a + n - 1 so
            - when a = 1 then b = n
            - when a = m - n + 1 then b = m
    '''