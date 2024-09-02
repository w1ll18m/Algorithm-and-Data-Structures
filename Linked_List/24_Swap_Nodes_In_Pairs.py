from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev, cur = dummy, head

        while cur is not None and cur.next is not None:
            next = cur.next
            cur.next = next.next
            next.next = cur
            prev.next = next

            prev = cur
            cur = cur.next

        return dummy.next

    '''
    swap every two adjacent nodes 
    if number of nodes is odd then leave the last node alone
    '''
        