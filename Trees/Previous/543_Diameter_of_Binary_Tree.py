# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.longestDiameter = 0

        def findMaxDepth(node):
            if node is None:
                return 0

            left_depth = findMaxDepth(node.left)
            right_depth = findMaxDepth(node.right)
            
            diameter = left_depth + right_depth
            if diameter > self.longestDiameter:
                self.longestDiameter = diameter

            return 1 + max(left_depth, right_depth)
        
        findMaxDepth(root)
        return self.longestDiameter

        '''
        observe that longest diameter is either:
            1. right depth + left depth of current node
            2. longest diameter of a subnode
        thus we need to keep track of longestDiameter for all nodes
        '''
