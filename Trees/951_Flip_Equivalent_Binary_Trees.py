from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # if both trees are empty then return False
        if not root1 and not root2:
            return True

        # case where both trees are not empty
        elif root1 and root2:
            # if root values are not same then return False
            if root1.val != root2.val:
                return False

            # check if subtrees are flip equivalent if we dont flip at current node 
            no_flip_equiv = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
            # check if subtrees are flip equivalent if we flip at current node
            flip_equiv = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)

            # tree is flip equivalent if subtrees are flip equivalent in either case (at least one DFS call will terminate immediately)
            return no_flip_equiv or flip_equiv

        # if one tree is empty but not the other then return False
        else:
            return False
    
    '''
    flip operation -> swap the left and right child subtrees
    x is flip equivalent to y if we can make x = y by flipping
    determine if 2 binary trees are flip equivalent

    need to visit each node, similar to equal tree -> DFS
    for 2 trees to be flip equivalent then (1) root node values must be equal
                                           (2) subtree at left/right children must be flip equivalent 
    lets write a recursive solution:
        - if node1 and node2 are None then return True
        - if node1.val != node2.val then return False
        - recurse to check if subtrees are flip equivalent if we flip at root or if we don't
            - one of these dfs calls will terminate immediately
            - we can't have both node1.left = node2.left and node1.left = node2.right (due to unique node values)
    we visit each node twice thus O(n) time complexity
    '''
        