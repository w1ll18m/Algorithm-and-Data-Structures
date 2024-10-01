from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, lNode, rNode):
        # if lNode == rNode == None -> retunr True
        if lNode is None and rNode is None:
            return True
        # if lNode != rNode -> return False
        elif lNode is None or rNode is None:
            return False
        elif lNode.val != rNode.val:
            return False
            
        # if lNode == rNode -> recurse of subtrees
        return self.isMirror(lNode.left, rNode.right) and self.isMirror(lNode.right, rNode.left)

    '''
    we need to traverse the entire tree -> dfs
    besides from the first node, this problem is equivalent to checking if the subtrees are mirrors
        - SIMILAR TO CHECKING IF 2 TREES ARE EQUAL
        - if lNode == rNode == None then return True
        - if lNode != rNode then return False
        - if lNode == rNode:
            - return dfs(lNode.left, rNode.right) and dfs(lNode.right, rNode.left)
            - mirror (1) left child of left tree is equal to right child of right tree
                     (2) right child of right tree is equal to left child of right tree
    '''
        