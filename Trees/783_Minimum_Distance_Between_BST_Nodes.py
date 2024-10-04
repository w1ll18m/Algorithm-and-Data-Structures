from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # initialize array to contain sorted values
        sortedArray = []

        def getSorted(node):
            if node is None:
                return
            
            # traverse left subtree first and add values to array
            if node.left: getSorted(node.left)
            # add current node value to array
            sortedArray.append(node.val)
            # traverse right subtree after and add values to array
            if node.right: getSorted(node.right)
        
        getSorted(root)

        # iterate through the array to calculate difference between adjacent elements
        min_dif = sortedArray[1] - sortedArray[0]
        for i in range(2, len(sortedArray)):
            dif = sortedArray[i] - sortedArray[i-1]
            if dif < min_dif:
                min_dif = dif
        
        return min_dif
    
    '''
    return the minimum difference between the values of any 2 nodes in the tree

    does not require a recursive solution -> minimum difference in subtree does not matter
    minimum distance -> sorted array then calculate difference between adjacent nodes
    note that we can create a sorted array easily from a binary tree through inorder traversal:
        - traverse left subtrees first and add to array
        - traverse current nodes next and add to array
        - traverse right nodes last and add to array
    thus O(n) to create sorted array and O(n) to calculate min difference with sorted array so O(n) time complexity total
    '''