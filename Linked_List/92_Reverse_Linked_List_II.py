from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        idx = 1
        before, cur = dummy, head

        # find the left node in the linked list
        while idx != left:
            before = cur
            cur = cur.next
            idx += 1
        
        # reverse the linked list from left to right
        prev = before
        while idx <= right:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            idx += 1
        
        # now cur should be the node after right and prev should be right
        left_node = before.next
        before.next = prev
        left_node.next = cur

        return dummy.next
        
    '''
    given left and right, reverse the nodes of the list from position left to position right
    note that the linked list is 1-indexed
    
    1. find the left node by keeping track of the index
    2. reverse the linked list from left to right -> 1 pass
    3. let the node before left point to right and left point to the node after right -> 2 operations
    initialize a dummy node just in case left is the head
    
    do we need to deal with the case that left == right? 
    '''
        