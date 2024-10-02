from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = {}
        duplicates = []

        def findDuplicates(node):
            # string representation of empty tree is ""
            if node is None:
                return ""
            
            # recurse on left subtree and right subtree to create string representation
            string_repr = f"{node.val} ({findDuplicates(node.left)}) ({findDuplicates(node.right)})"

            # if subtree does not exist in hashtable, then add it
            if string_repr not in subtrees:
                subtrees[string_repr] = [node, False]
            # if subtree exists in hashtable but not in duplicates array, then add it
            elif not subtrees[string_repr][1]:
                # set second value of tuple to True to represent that it has been added to the duplicates array
                subtrees[string_repr][1] = True
                duplicates.append(subtrees[string_repr][0])

            return string_repr
        
        findDuplicates(root)
        return duplicates
    
    '''
    return all duplicate subtrees in a binary tree
    
    solution #1: iteratively compare all subtrees 
        - there are n subtrees (one for each node)
        - for each of the subtree, we have to compare it to all other subtrees
        - comparing 2 trees takes O(n) time
    thus the time complexity of this solution is O(n^3) -> VERY BAD

    solution #2: leverage hash mapping
        - finding duplicates seems like a hashing problem
            - add subtree to hashtable 
            - check if subtree already exists in hashtable
        - can we compare 2 trees in O(1) time? -> convert to string representation
            - preorder representation -> (root (left) (right))
        - how can we ensure that only one root node of subtree is returned?
            - hashtable consists of string_representation -> (root, False)
            - first value of tuple represents the root node of the subtree
            - second value of tuple represents if subtree is added to list of duplicates
    '''