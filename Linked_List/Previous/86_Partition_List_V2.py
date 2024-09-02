from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(-101, head)
        last, prev, cur = dummy, dummy, head


        while cur is not None:
            if cur.val < x:
                if prev.val >= x: 
                    prev.next = cur.next
                    cur.next = last.next
                    last.next = cur

                    last = cur
                    cur = prev.next
                else:
                    last = cur
                    prev = cur
                    cur = cur.next
            else:
                prev = cur
                cur = cur.next
        
        return dummy.next

    '''
    given a linked list and value x, partition it such that all nodes less than x come before nodes greater/equal to x
    preserve the original relative order of the nodes -> use a stack

    solution #1: keep 2 stacks for nodes lesser and greater -> O(n) time complexity and O(n) space complexity
        - iterate through the list and add each nodes to the corresponding stack based on their value and x -> O(n)
        - reconstruct two linked lists from the two stacks -> O(n)
        - let the last node of the lesser list point to the first node of the greater list -> O(1)
    
    solution #2: maintain 2 pointers where one of the pointers is the last valid node -> O(n) time complexity and O(1) space complexity
        - keep a pointer for the last node less than x
        - iterate through the list and if we encounter a node less than x then remove it and add it behind last node less than x
            - set last node less than x to the new node less than x
    '''
        