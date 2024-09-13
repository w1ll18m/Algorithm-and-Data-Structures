from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy represents the beginning of the sorted list
        dummy = ListNode(0, head)

        # iterate through input list and find location it belongs in sorted list
        cur = head.next
        head.next = None    # NEED TO SET END OF SORTED LIST TO NONE TO PREVENT CYCLES
        while cur is not None:
            next = cur.next

            sorted_cur = dummy.next
            sorted_prev = dummy
            # iterate through sorted list to find correct place
            while sorted_cur is not None:
                # cur is less than sorted_cur -> insert cur before sorted_cur
                if cur.val <= sorted_cur.val:
                    sorted_prev.next = cur
                    cur.next = sorted_cur
                    break
                
                # cur is greater than last node -> insert cur at end of sorted list
                if sorted_cur.next is None:
                    sorted_cur.next = cur
                    cur.next = None     # NEED TO SET END OF SORTED LIST TO NONE TO PREVENT CYCLES
                    break
                
                sorted_prev = sorted_cur
                sorted_cur = sorted_cur.next
            
            cur = next

        return dummy.next
                    


        