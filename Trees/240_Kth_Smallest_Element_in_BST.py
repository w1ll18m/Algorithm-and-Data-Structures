from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root

        counter = k

        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                counter -= 1
                if counter == 0:
                    return cur.val
                cur = cur.right
                
    '''
    use inorder iterative traversal since all we are basically doing is counting nodes
    '''
        