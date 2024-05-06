# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        self.isBalanced = True

        def maxDepth(node):
            if node is None:
                return 0
            left_depth = maxDepth(node.left)
            right_depth = maxDepth(node.right)
            if abs(left_depth - right_depth) > 1:
                self.isBalanced = False
            return 1 + max(left_depth, right_depth)
        
        maxDepth(root)
        return self.isBalanced
        
        '''
        note that we need to keep track of both the depth of each node as well as if its subnodes are balanced
        thus we track depth of subnodes through recursive function and if subnodes are balanced with class field
        '''