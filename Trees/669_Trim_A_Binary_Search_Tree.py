from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def removeSmaller(node):
            if node is None:
                return None
            
            # if node.val >= low then recurse on left subtree
            if node.val >= low:
                node.left = removeSmaller(node.left)
                return node
            # if node.val < low then replace current node with trimmed right subtree
            else:
                return removeSmaller(node.right)
        
        def removeBigger(node):
            if node is None:
                return None
            
            # if node.val <= high then recurse on right subtree
            if node.val <= high:
                node.right = removeBigger(node.right)
                return node
            # if node.val > high then replace current node with trimmed left subtree
            else:
                return removeBigger(node.left)
        
        # remove elements smaller than low from tree then elements greater than high
        return removeBigger(removeSmaller(root))

    '''
    we want to remove all nodes less than low and greater than high

    we will first recursively remove all nodes less than low
        - if node is None then return None
        - if node.val >= low then recurse on left subtree
        - if node.val < low
            - all values in left subtree are removed due to BST properties
            - replace the current node with the root of the trimmed right subtree
    
    we will then recursively remove all nodes greater than low
        - if node is None then return None
        - if node.val <= high then recurse on right subtree
        - if node.val > high
            - all values in right subtree are removed due to BST properties
            - replace the current node with the root of the trimmed left subtree
    
    since we visit each node at most 2 times then the time complexity is O(n)
    '''