# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        sum_list = ListNode()
        cur = sum_list
        carry_over = 0

        while l1 is not None or l2 is not None:
            if l1 is not None and l2 is not None:
                sum = l1.val + l2.val + carry_over
                l1 = l1.next
                l2 = l2.next
            elif l1 is not None:
                sum = l1.val + carry_over
                l1 = l1.next
            else:
                sum = l2.val + carry_over
                l2 = l2.next

            carry_over = sum / 10
            sum = sum % 10

            sum_digit = ListNode(sum, None)
            cur.next = sum_digit
            cur = sum_digit
        
        if carry_over == 1:
            sum_digit = ListNode(1, None)
            cur.next = sum_digit
        
        return sum_list.next

    '''
    traverse both linked lists at the same rate using pointers
    at each step, add the 2 values together and store the result value in the new linked list
        - if the value is greater or equal to 10, store the ones digit and carry over
        - add the carry over (if it exists) when adding the 2 values 
        - if one of the lists are empty then treat the value as a 0
    if space complexity matters, we can store the result on top of one of the existing linked lists
    '''