from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dec_list = []
        cur = head

        # iterate through the list and create a monotonically decreasing stack
        while cur is not None:
            while True:
                # case when current node is less/equal to top of stack (or stack is empty)
                if len(dec_list) == 0 or cur.val <= dec_list[-1].val:
                    dec_list.append(cur)
                    break
                # case when current node is greater than top of stack
                else:
                    dec_list.pop(-1)
            cur = cur.next
        
        # reconstruct new list by popping from the stack (where top of stack is end of list)
        while len(dec_list) != 0:
            prev = dec_list.pop(-1)
            prev.next = cur
            cur = prev
        
        return cur
    
    '''
    remove every node which has a node with a greater value anywhere to the right side of it

    thus we should have a monotonically decreasing linked list as the output

    iterate through the list keep track of:
        - modified list head value
        - modified list current value

    if we encounter a node that:
        - is less than modified list current value -> keep that node and set current value to it
        - is less than modified list head but greater than current value -> how do we go back and remove those nodes????
            - keep a MONOTONICALLY DECREASING STACK
                - allows us to go back to previous entries in the linked list
        - is greater than modified list head -> set modified list head to current node (which effectively removes all nodes to left)
    
    5 2 1  -> dont remove any nodes
    5 2 3  -> remove 2
    5 2 13 -> remove 5 2 

    lets revise our solution to use a monotonically decreasing stack
    iterate through the list and construct a monotonically decreasing stack:
        - if current node is greater than top of stack then keep popping from stack until its smaller
        - if current node is smaller than top of stack then add it to the stack
    reconstruct new list by popping from the stack
    '''