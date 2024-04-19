# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = None
        cur = head
        while cur != None:        
            next = cur.next             
            cur.next = prev             # let current node point to previous node

            prev = cur                  # the current node becomes the previous node
            cur = next                  # the next node becomes the current node

        return prev                     # cur = None
            
        