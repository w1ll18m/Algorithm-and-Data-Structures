from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # initialize k dummy nodes that point to the head of each of the k new lists
        dummys = [None] * k
        tails = [None] * k
        for i in range(k):
            dummys[i] = ListNode(0, None)
            tails[i] = dummys[i]
        
        # count the number of nodes in the linked list
        cur = head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        
        # calculate the number of nodes in the k new lists
        nodes_per_list = count // k
        nof_extra_nodes = count % k

        cur = head
        for i in range(k):
            dummys[i].next = cur

            # list should have at least n // k (consecutive) nodes
            for j in range(nodes_per_list):
                tails[i] = cur
                cur = cur.next

            # first n % k nodes will have an extra node
            if nof_extra_nodes != 0:
                tails[i] = cur
                cur = cur.next
                nof_extra_nodes -= 1

        # set the last node of each new list to point to None
        for i in range(k):
            tails[i].next = None
            dummys[i] = dummys[i].next
        
        return dummys

    '''
    given the head of a linked list, split the linked list into k consecutive linked list parts
    parts should be in order of occurence -> use dummy nodes to keep track of k lists!!!

    count the number of nodes in the linked list -> O(n)
    initialize k dummy nodes that point to the head of each of the k new lists
    calculate the number of nodes in each of the k new lists
        - each list has at least n // k nodes
        - if n % k != 0 then the first n % k lists will have an extra node
    iterate through the linked list and append the calculated # of nodes to each linked list -> O(n)
        - remember to set the last node of each new list to point to None
    '''
        