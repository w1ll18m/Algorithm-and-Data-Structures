from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def rflatten(head):     # this function should never be called with an empty node
            # initialize pointers to the current node and tail node
            cur, tail = head, None

            # iterate through nodes of the same level
            while cur is not None:
                next_node = cur.next

                # if next node is none then current node could be the tail (if current node has no child pointer)
                if next_node is None:
                    tail = cur

                # recursively flatten the child list if it exists
                if cur.child is not None:
                    flat_head, flat_tail = rflatten(cur.child)
                    cur.child = None

                    # connect the current node and the head of the flattened child list
                    cur.next = flat_head
                    flat_head.prev = cur

                    # connect the next node and the tail of the flattened child list
                    flat_tail.next = next_node
                    if next_node is not None:
                        next_node.prev = flat_tail
                    else:
                        tail = flat_tail
                
                cur = next_node
            
            return head, tail
        
        if head is None:
            return None
        flat_head, flat_tail = rflatten(head)
        return flat_head
    
    '''
    doubly linked list -> contains nodes with "next" pointer, "previous" pointer, and "child" pointer
        - "child" pointer may point to a seperate doubly linked list
    given the head, flatten the list so:
        (i) all nodes appear in a single-level doubly linked list
        (ii) nodes in the child list should appear after curr and before curr.next 
    
    observe that this a recursive problem -> each child could be a multilevel doubly linked list that needs to be flattened too
    base case 1: cur is None then return None
    base case 2: cur is not None but cur.child is None then recurse on cur.next
    case 3: cur is not None and cur.child is not None
        - suppose that we recurse on cur.child which returns the head to a flattened list
        - then set cur.next to the head of the flattened list that was returned by the recursive function
        - how do we set the end of the flattened list to cur.next? -> iterate through flattened child list to find its tail

    but observe that we might visit each node more than once (since we are iterating through flattened child list to find its tail) -> time complexity of O(n^2)
    to avoid this issue, we should return the head and tail of each flattened list so we would visit each node at most once! -> time complexity of O(n)
        - let's recurse on the head of each linked list level and iterate through nodes of the same level!!!
        - if cur.child is not None then recurse on the head of the child list which will return the head + tail of the flattened child list
        - if cur.next is None and cur.child is None then cur is the tail node of the flattened list
        - if cur.next is None and cur.child is not None then the tail of flattened child list is the tail node of the flattened list
    '''