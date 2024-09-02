from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nstack = []
        cur = head

        while cur is not None:
            nstack.append(cur)
            cur = cur.next
        
        nstack.sort(key=lambda x: x.val)
        
        prev = None
        while len(nstack) != 0:
            cur = nstack.pop()
            cur.next = prev
            prev = cur

        return prev
    
    '''
    solution #1: use an array of nodes and merge sort -> O(nlogn) time complexity and O(n) space complexity
        - sort based on node.val
        - reconstruct the linked list by popping all the nodes off the array
    '''