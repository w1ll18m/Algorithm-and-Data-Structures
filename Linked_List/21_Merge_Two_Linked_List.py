# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # initalize the new list with the head being a dummy node
        head = ListNode()
        cur = head

        # append larger node to the new list
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
        
        # at this point either list1 or list2 is empty (or both) so append the remaining list
        if list1 is not None:
            cur.next = list1
        elif list2 is not None:
            cur.next = list2
        
        # head is dummy node so return the next node
        return head.next
                

            
        