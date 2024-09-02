from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # case: list of length 0 or 1
        if head is None or head.next is None:
            return head
        
        # find the middle node using fast/slow pointers
        slow, fast = head, head.next
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # recurse on both sides of the list
        list1 = head
        list2 = slow.next
        slow.next = None

        sorted1 = self.sortList(list1)
        sorted2 = self.sortList(list2)

        # combine by merging the two sorted lists
        return self.combine(sorted1, sorted2)
  
    def combine(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        
        while True:
            if list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next

            elif list1 is not None:
                cur.next = list1
                list1 = list1.next
                cur = cur.next

            elif list2 is not None:
                cur.next = list2
                list2 = list2.next
                cur = cur.next

            else:
                cur.next = None
                break
        
        return dummy.next
    
    '''
    solution #1: use an array of nodes and merge sort -> O(n log n) time complexity and O(n) space complexity
        - sort based on node.val
        - reconstruct the linked list by popping all the nodes off the array

    solution #2: implement modified merge sort on linked list -> O(n log n) time complexity and O(log n) space complexity
        - find the middle node using fast/slow pointers
        - recurse on both sides of the list
        - combine by merging two sorted lists
    note that the space used by the call stack during the recursive calls is log n
        - solution is O(1) space complexity if space for stack is not counted
    '''