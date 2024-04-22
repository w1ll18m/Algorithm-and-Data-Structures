# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head is None:
            return False
        
        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False

    '''
    maintain a fast pointer and a slow pointer (fast moves 2 nodes and slow moves 1 node at a time)
    if there is not cycle then the fast pointer should eventually reach end of list (represented as None)
    if there is a cycle then eventually the fast pointer and slow pointer should meet
    '''
        