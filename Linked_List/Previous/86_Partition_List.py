from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # iterate through the list and add nodes to corresponding stack
        lstack, gstack = [], []
        cur = head

        while cur is not None:
            if cur.val < x:
                lstack.append(cur)
            else:
                gstack.append(cur)
            cur = cur.next
        
        # reconstruct the two linked lists from the two stacks
        lprev = None
        while len(lstack) != 0:
            cur = lstack.pop()
            cur.next = lprev
            lprev = cur
        
        gprev = None
        while len(gstack) != 0:
            cur = gstack.pop()
            cur.next = gprev
            gprev = cur
        
        # let the last node of the llist point to first node of glist
        if lprev is None:
            return gprev
        if gprev is None:
            return lprev
        
        prev = lprev
        cur = lprev.next
        while cur is not None:
            prev = cur
            cur = cur.next

        prev.next = gprev

        return lprev

    '''
    given a linked list and value x, partition it such that all nodes less than x come before nodes greater/equal to x
    preserve the original relative order of the nodes -> use a stack

    keep 2 stacks for nodes lesser and greater
    iterate through the list and add each nodes to the corresponding stack based on their value and x -> O(n)
    reconstruct two linked lists from the two stacks -> O(n)
    let the last node of the lesser list point to the first node of the greater list -> O(1)

    thus the total time complexity of our solution becomes O(n)
    '''
        