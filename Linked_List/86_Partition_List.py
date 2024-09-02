from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        llist, glist = ListNode(), ListNode()
        lcur, gcur = llist, glist
        cur = head

        # iterate through list and add nodes to corresponding sublists
        while cur is not None:
            print(cur.val)
            if cur.val < x:
                lcur.next = cur
                lcur = cur
            else:
                gcur.next = cur
                gcur = cur
            cur = cur.next
        
        # let the last node of llist point to first node of glist
        lcur.next = glist.next
        gcur.next = None

        return llist.next

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
    
    solution #3: maintain 2 seperate list for nodes lesser and greater -> O(n) time complexity and O(n) space complexity
        - basically the same thing as solution #1 but lists dont need to be reconstructed from array
    '''
        