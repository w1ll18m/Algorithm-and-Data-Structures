from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, cur = None, head
        new_head = None

        while cur is not None:
            if cur.val == val:
                # Case 1: prev is not None then remove the current node
                if prev is not None:
                    prev.next = cur.next
                # Case 2: prev is None then current node is not head
            else:
                if prev is None:
                    new_head = cur
                prev = cur

            cur = cur.next
        
        return new_head

        