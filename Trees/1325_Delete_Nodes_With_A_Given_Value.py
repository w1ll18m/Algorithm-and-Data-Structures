from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # if node is None then return None
        if root is None:
            return None

        # recurse on subtrees
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        # if node is Leaf and node.val == target then remove it
        if root.left is None and root.right is None and root.val == target:
            return None
        else:
            return root
        
    '''
    need to check all nodes -> DFS
    lets build a recursive solution
        - if node is None then return None
        - if node is a leaf (and node.val == target) then delete it (return None)
        - if node is not a leaf then
            - recurse on left and right subtrees
            - if it is now a leaf (and node.val == target) then delete it (return None)
            - otherwise don't delete it (return node)
    we can actually recurse on subtrees before checking if node is a leaf
        - leaf has empty subtrees that return None when recursed on
    we visit each node exactly once thus O(n) time complexity and O(1) space complexity
    '''
        