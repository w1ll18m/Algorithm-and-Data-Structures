# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        dummy = ListNode(0, head)
        cur = dummy

        # Step 1: find the node right before the left node
        count = 0
        while count != left - 1:
            cur = cur.next
            count += 1
        
        # Step 2: let prev be the node right before the left node or dummy if left is 1
        prev = cur
        if left == 1:
            prev = dummy

        # Step 3: increment the current node to be the left node (keep track of left node and node before it)
        before_left_node = cur
        left_node = cur.next
        cur = cur.next
        count += 1

        # Step 4: reverse all of the nodes until the right node (keep track of right node and node after it)
        while count <= right:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            count += 1

        right_node = prev
        after_right_node = cur

        # Step 5: let before_left_node point to right_node and let left_node point to after_right_node (handle None cases)
        left_node.next = after_right_node
        before_left_node.next = right_node

        return dummy.next

        '''
        keep count of the current node and iterate to the left node
        record the node before the left node 
            - need to handle case where this node is None
        reverse the linked list between the left node and the right node
        '''
        