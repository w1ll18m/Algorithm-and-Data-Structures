
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        mapping = dict()

        # Step 1: deep copy the linked list following the next pointer + create mapping
        def copyRegularList(head):
            if head is None:
                return None
            tail = copyRegularList(head.next)
            new = Node(head.val, tail, random=None)
            mapping[head] = new
            return new
        
        copy = copyRegularList(head)

        cur = head
        copycur = copy

        # Step 2: for each old_node, find new_node.random by using old_node.random to index the mapping
        while cur is not None:
            if cur.random is None:
                copycur.random = None
            else:
                copy_random = mapping[cur.random]
                copycur.random = copy_random
            cur = cur.next
            copycur = copycur.next
        
        return copy
            
        
'''
linked list but each node has pointer to random node
construct a deep copy of the list (n brand new nodes)

attempt 1:
iterate through the list twice
    - first time constructing the initial nodes with no random pointer
    - second time adding the random node pointer the second time through
Q: in the second iteration, how do I reach the node that the random pointer needs to point to?

attempt 2:
observe that when performing a deep copy of a regular linked list, we recursively build the rest of the list first
    - ex) if we want to deep copy 1 -> 2 -> 3 -> 4, we create nodes 2 -> 3 -> 4 before we create node 1
thus try recursively building the rest of the list first too (following both the random and next pointers)
Q: how do we ensure that a node isnt created multiple times while following both the random and next pointers?

attempt 3:
during the first iteration, deep copy the linked list by following the next pointers (ignore random pointers)
during the second iteration, for each old_node, iterate through both the original and copy until we find the node that matches the random pointer -> O(n^n) time

attempt 4 (using hint 3):
hint 3 says to use extra space to keep a mapping of old_node -> new_node to prevent creating multiple copies of the same node
during the first iteration, deep copy the linked list by following the next pointers but keep a dictionary mapping old_node to new_node
during the second iteration, for each old_node, we find the new_node.random associated with old_node.random using the mapping -> O(n) time
'''