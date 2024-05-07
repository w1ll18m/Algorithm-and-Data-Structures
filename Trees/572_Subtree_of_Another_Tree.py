# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if subRoot is None:
            return True
        elif root is None:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def sameTree(self, node, subnode):
        if node is None and subnode is None:
            return True
        elif node and subnode and node.val == subnode.val:
            return self.sameTree(node.left, subnode.left) and self.sameTree(node.right, subnode.right)
        else:
            return False
    
    '''
    this solution is O(n*m) where n is # of nodes in root and m is # of nodes in subRoot
    '''