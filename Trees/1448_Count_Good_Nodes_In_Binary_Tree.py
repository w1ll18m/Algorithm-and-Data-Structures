# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return 1 + self.isGoodNode(root.left, root.val) + self.isGoodNode(root.right, root.val)
    
    def isGoodNode(self, node, max):
        if not node:
            return 0
        if node.val >= max:
            return 1 + self.isGoodNode(node.left, node.val) + self.isGoodNode(node.right, node.val)
        return self.isGoodNode(node.left, max) + self.isGoodNode(node.right, max)
        