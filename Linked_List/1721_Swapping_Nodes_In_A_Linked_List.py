from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        a, b = head, head
        prev_a, prev_b = dummy, dummy

        # find the kth node from the beginning
        for i in range(k - 1):
            prev_b = b
            b = b.next
        k_begin = b
        prev_begin = prev_b

        # find the kth node from the end (aka the n - k + 1 node)
        idx_b = k
        while b.next is not None:
            b = b.next
            idx_b += 1

            prev_a = a
            a = a.next
        k_end = a
        prev_end = prev_a
        
        # if the kth node from the beginning and end are the same then no swap is needed
        if k == idx_b - k + 1:
            return dummy.next
        # if the kth node from the beginning is right before the kth node from the end
        elif k == idx_b - k:
            prev_begin.next = k_end
            k_begin.next = k_end.next
            k_end.next = k_begin
        # if the kth node from the beginning is right after the kth node from the end
        elif k == idx_b - k + 2:
            prev_end.next = k_begin
            k_end.next = k_begin.next
            k_begin.next = k_end
        # if the kth node from the beginning is not adjacent to the kth node from the end
        else:
            prev_begin.next = k_end
            prev_end.next = k_begin
            temp = k_end.next
            k_end.next = k_begin.next
            k_begin.next = temp
        
        return dummy.next

    '''
    swap the values of the kth node from the beginning and the kth node from the end (1-indexed)
    
    idea #1: O(n) time complexity and O(n) space complexity
    maintain a stack of nodes to allow traversal back through the list -> O(n) space complexity
    iterate through the list and keep track of the kth node from the beginning -> O(n)
    pop k nodes from the stack to get the kth node from the end -> O(n) 
    swap the two nodes -> O(1)

    idea #2: O(n) time complexity and O(1) space complexity
    iterate through the list and keep track of the kth node from the beginning -> O(n)
    reverse the linked list -> O(n)
    iterate through the reversed list and keep track of the kth node from the beginning (this gives us kth node from the end) -> O(n)
    swap the two nodes -> O(1)
    reverse the linked list again -> O(n)

    idea #3: O(n) time complexity and O(1) space complexity
    iterate through the list and keep track of the kth node from the beginning -> O(n)
    find the kth node from the end using 2 pointer strategy -> O(n)
    when swapping, need to consider the cases when index of the 2 nodes are adjacent or the same
    '''
        