from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        numTree = self.constructNumTree(root)
        return self.findKthSmallest(root, numTree, k)
    
    def constructNumTree(self, node):
        if node is None:
            return None
        leftNode = self.constructNumTree(node.left)
        rightNode = self.constructNumTree(node.right)

        nofnodes = 1
        if leftNode is not None:
            nofnodes += leftNode.val
        if rightNode is not None:
            nofnodes += rightNode.val
        
        newNode = TreeNode(nofnodes, leftNode, rightNode)
        return newNode
    
    def findKthSmallest(self, node, numnode, k):
        if numnode.left is not None:
            leftcount = numnode.left.val
        else:
            leftcount = 0
        
        if k == leftcount + 1:
            return node.val
        elif k < leftcount + 1:
            return self.findKthSmallest(node.left, numnode.left, k)
        else:
            return self.findKthSmallest(node.right, numnode.right, k - leftcount - 1)
    
    '''
    construct a new tree where each node corresponds to the original tree but with the following changes:
        - the value is the number of nodes in the subtree starting at that node
    [note that constructing this tree takes O(n) time]
    then we can easily search for the kth smallest value by looking at the number of nodes in a root's left and right subtrees
    [note that this should take O(log n) time since it is a BST tree]
    '''
        