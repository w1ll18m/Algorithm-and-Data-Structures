from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # if there are nodes then return None
        if len(inorder) == 0:
            return None
        
        # the first element of the preorder list is the root
        root = preorder[0]
        # find the index of the root in the inorder list
        root_idx = inorder.index(root)

        # build the inorder lists of the left and right subtrees
        left_inorder = inorder[0:root_idx]
        right_inorder = inorder[root_idx + 1:]

        # build the preorder lists of the left and right subtrees
        nofright = len(right_inorder)
        right_preorder = preorder[len(preorder) - nofright:]
        left_preorder = preorder[1:len(preorder) - nofright]

        return TreeNode(root, self.buildTree(left_preorder, left_inorder), self.buildTree(right_preorder, right_inorder))

    '''
    observe that preorder is current left right
                 inorder is left current right

    preorder -> [3 9 20 15 7]
    inorder -> [9 3 15 20 7]

    - observe that the first element of the preorder list is the root
    - then iterate through inorder list until we find the root -> O(n)
    - we can split the inorder list into [9] and [15 20 7]
        - represents the inorder list of the left and right subtrees
    - preorder visits all of the left nodes before right nodes
        - the last 3 nodes of the preorder list represents the preorder list of the subtree

    using these observations, we can recursively build the binary tree in O(n^2) time
    '''
        