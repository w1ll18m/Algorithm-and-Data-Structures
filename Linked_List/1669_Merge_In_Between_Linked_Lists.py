# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        pa, pb = list1, list1
        
        # iterate 2 pointers to the a-1th node and b+1th node 
        for i in range(a - 1):
            pa = pa.next
        for i in range(b + 1):
            pb = pb.next
        
        plast = list2
        while plast.next is not None:
            plast = plast.next 
        
        # set next of a-1th node to first node of list2
        pa.next = list2

        # set next of last node of list2 to the b+1st node
        plast.next = pb

        return list1
    
    '''
    remove list1's nodes from the ath node to the bth node
    replace those nodes with list2 in their place

    iterate 2 pointers to the a-1th node and the b+1th node respectively
    set next of a-1th node to first node of list2
    set next of last node of list2 to the b+1st node
    '''