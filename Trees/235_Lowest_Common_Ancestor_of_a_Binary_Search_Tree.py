# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < q.val:
            lower = p
            upper = q
        else:
            lower = q
            upper = p
        
        return self.findLCA(root, lower, upper)
    
    def findLCA(self, root, lower, upper):
        if not root:
            return None
        elif lower.val <= root.val and upper.val >= root.val:
            return root
        else:
            return self.findLCA(root.left, lower, upper) or self.findLCA(root.right, lower, upper)

    '''
    binary search tree -> left subtree < root and right subtree > root
    a node is considered the LCA <==> p and q are not both in the same subtree <==> node is less than p and greater than q
    '''