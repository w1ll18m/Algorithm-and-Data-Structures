from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        head1, head2 = head, None

        # Find midpoint using fast/slow pointers
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        midpoint = slow.next

        # Reverse the linked list of the latter half
        prev, cur = None, midpoint
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        head2 = prev

        # Add twin values by iterating through linked list of each half
        max_twin_sum = 0
        while head1 is not None and head2 is not None:
            twin_sum = head1.val + head2.val
            max_twin_sum = max(max_twin_sum, twin_sum)
            head1, head2 = head1.next, head2.next
        
        return max_twin_sum

    '''
    find midpoint using fast/slow pointers -> O(n)
    reverse linked list of latter half -> O(n)
    add up twin values by iterating through linked list of each half -> O(n)
    '''