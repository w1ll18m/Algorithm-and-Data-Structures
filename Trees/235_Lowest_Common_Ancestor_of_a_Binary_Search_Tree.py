# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.findLCA(root, min(p.val, q.val), max(p.val, q.val))
    
    def findLCA(self, node, lower, upper):
        if lower <= node.val <= upper:
            return node
        elif node.val < lower:
            return self.findLCA(node.right, lower, upper)
        else:
            return self.findLCA(node.left, lower, upper)

    '''
    binary search tree -> left subtree < node and right subtree > node
    a node is considered the LCA <==> p and q are not both in the same subtree <==> node is less than p and greater than q
    if current node is less than p and q then search to the right
    if current node is greater than p and q then search to the left
    '''