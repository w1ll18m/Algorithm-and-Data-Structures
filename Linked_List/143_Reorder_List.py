# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        # Step 1: find the middle node using slow and fast pointers
        start = head
        slow = head
        fast = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        middle = slow

        # Step 2: reverse the second half of the list

        prev = None
        end = middle.next
        middle.next = None

        while end is not None:
            temp = end.next
            end.next = prev
            prev = end
            end = temp
        end = prev
        
        # Step 3: merge the first half of the list and the second half of the list

        counter = 1
        cur = ListNode()
        while start is not None or end is not None:
            if counter % 2 != 0:
                cur.next = start
                start = start.next
            else:
                cur.next = end
                end = end.next
            cur = cur.next
            counter += 1
        
        return head

        '''
        find the middle node (denoted Lk) using fast and slow pointer technique
        first half of the list (L1 to Lk) is already sorted so we just need to sort the second half of the list (Lk+1 to Ln)
            - reverse linked list from Lk to Ln
        create new linked list by alternating nodes from first half and second half of the list
        '''
        