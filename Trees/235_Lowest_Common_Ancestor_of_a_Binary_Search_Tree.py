# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while True:
            # current node is not LCA, traverse to left subtree
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left
            # current node is not LCA, traverse to right subtreez
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right
            # conditions are not true so current node is LCA
            else:
                return cur
    
    '''
    given a binary search tree, find the lowest common ancestor of 2 given nodes
    assume that p and q will exist in the BST,s p != q, and all node.val are unique

    observe that for a given node n:
        - n is not the LCA if n.val > p and n.val > q
            - traverse to the left subtree
        - n is not the LCA if n.val < p and n.val < q
            - traverse to the right subtree
    so we traverse the list until we find the first node such that those conditions are not true -> O(log n)
    '''