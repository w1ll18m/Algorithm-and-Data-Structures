# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        pointer_a = head
        pointer_b = head
        for i in range(n):                  # create an offset of n between pointer_a and pointer_b
            pointer_b = pointer_b.next

        prev = None                         # keep track of the node before pointer_a
        while pointer_b is not None:
            prev = pointer_a
            pointer_a = pointer_a.next
            pointer_b = pointer_b.next
        
        if prev == None:                    # if prev == None then we are removing the first node
            return pointer_a.next
        else:                               # remove pointer_a which is the node after prev
            prev.next = prev.next.next
        return head
        
        '''
        observe that the nth node from the end of the list has index sz - n + 1
        we use 2 different pointers with an offset of n
            - when pointer_b = n + 1 then pointer_a = 1
            - when pointer_b = None (sz + 1) then pointer_a = sz - n + 1
        '''