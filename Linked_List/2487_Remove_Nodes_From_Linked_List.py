from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse the linked list
        prev, cur = None, head

        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        # iterate through the reversed list and construct the modified list
        last_valid = prev
        cur = last_valid.next
        last_valid.next = None

        while cur is not None:
            if cur.val >= last_valid.val:
                next = cur.next
                cur.next = last_valid
                last_valid = cur
                cur = next
            else:
                cur = cur.next
        
        return last_valid

    '''
    remove every node with a node with a greater value to its right

    we cant just make a monotonically decreasing list starting from the first node since it might not be the largest node
    but observe that the last node of the list will always be in the modified linked list since it has no nodes to its right
    thus the last node of the list will always be the smallest node in the modified linked list

    reverse the linked list then iterate through it
        - keep track of the last valid node and its value
        - if the current node is greater than the last valid node then add it to the modified linked list

    O(n) time complexity and O(1) space complexity
    '''