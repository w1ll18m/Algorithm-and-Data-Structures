from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # there is only 1 integer thus there is only 1 node
        if len(inorder) == 1:
            return TreeNode(inorder[0], None, None)
        
        # the last node of the postorder list is the root of the tree
        root = postorder[-1]

        # find the index of the root in the inorder list
        root_idx = 0
        for i in range(len(inorder)):
            if inorder[i] == root:
                root_idx = i
                break
        
        # create the inorder lists for left and right subtrees
        left_inorder = inorder[0:root_idx]
        right_inorder = inorder[root_idx + 1:]

        # case where left subtree is empty but not right subtree
        if len(left_inorder) == 0:
            right_postorder = postorder[:len(postorder) - 1]
            right_subtree = self.buildTree(right_inorder, right_postorder)
            return TreeNode(root, None, right_subtree)
        
        # case where right subtree is empty but not left subtree
        if len(right_inorder) == 0:
            left_postorder = postorder[:len(postorder) - 1]
            left_subtree = self.buildTree(left_inorder, left_postorder)
            return TreeNode(root, left_subtree, None)
        
        # create the postorder lists for left and right subtrees
        left_postorder = postorder[0:len(postorder) - len(right_inorder) - 1]
        right_postorder = postorder[len(postorder) - len(right_inorder) - 1:len(postorder) - 1]

        # recursively create the left and right subtrees
        left_subtree = self.buildTree(left_inorder, left_postorder)
        right_subtree = self.buildTree(right_inorder, right_postorder)

        return TreeNode(root, left_subtree, right_subtree)

    '''
    inorder traversal -> left current right
    postorder traversal -> left right current

    last node in postorder list is root
        - find index of root in inorder list
        - all elements with smaller index is in the left subtree
        - all elements with larger index is in the right subtree
    

    ITERATION 1:
    inorder -> [9 3 15 20 7]
    preorder -> [9 15 7 20 3]

    3 IS THE ROOT
        - find the index of integer 3 in the inorder list -> O(n)
            - [9] are nodes in left subtree 
            - [15 20 7] are nodes in the right subtree
        - [9 15 7 20] is the postorder list
            - observe in postorder traversal, left subtree will be visited before right subtree
            - last 3 nodes in postorder list are the right subtree nodes
        - recursively build the tree as follows:
            - left subtree -> inorder [9] and postorder [9]
            - right subtree -> inorder [15 20 7] and postorder [15 7 20]
    

    ITERATION 2:
    inorder -> [15 20 7]
    preorder -> [15 7 20]

    20 IS THE ROOT
        - find the index of integer 20 in the inorder list
            - [15] are nodes in the left subtree
            - [7] are nodes in the right subtree
        - recursively build the tree as follows:
            - left subtree -> inorder [15] and postorder [15]
            - right subtree -> inorder [7] and postorder [7]
    

    ITERATION 3:
    inorder -> [15]
    preorder -> [15]

    15 IS THE ROOT
        - [] are nodes in the left subtree
        - [] are nodes in the right subtree 
    THUS WE SHOULD STOP RECURSING


    Case 1: right subtree is empty but left subtree is not
    inorder -> [9 3]
    preorder -> [9 3]

    3 IS THE ROOT
        - [9] are nodes in the left subtree
        - [] are nodes in the right subtree
    then observe that inorder traversal visits the root last


    Case 2: left subtree is empty but right subtree is not
    inorder -> [3 15 20 7]
    postorder -> [15 7 20 3]
    then observe that inorder traversal visits the root first

    THUS THE TOTAL TIME COMPLEXITY IS O(N^2) SINCE WE VISIT EACH NODE ONCE AND ITERATE THROUGH A LIST OF LENGTH N AT EACH NODE
    '''