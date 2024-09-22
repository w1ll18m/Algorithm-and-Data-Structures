from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def getLeafs(node):
            if node is None:
                return []

            if node.left is None and node.right is None:
                return [node.val]
            else:
                return getLeafs(node.left) + getLeafs(node.right)
        
        leaf_list_1 = getLeafs(root1)
        leaf_list_2 = getLeafs(root2)
        return leaf_list_1 == leaf_list_2
    
    '''
    we want to see if the leafs from left to right are the same between nodes
    recursively generate list of leafs of each tree:
        - if node is a leaf then return [node.val]
        - if node is not a leaf then concatenate left leaf list and right leaf list and return it
        - if node is none then return empty list []
    '''
        