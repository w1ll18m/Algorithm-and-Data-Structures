import collections
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nextq = collections.deque()
        if root:
            nextq.append(root)
        right_view = []

        while nextq:
            for i in range(len(nextq) - 1):
                cur_node = nextq.popleft()
                if cur_node.left:
                    nextq.append(cur_node.left)
                if cur_node.right:
                    nextq.append(cur_node.right)

            right_node = nextq.popleft()
            
            if right_node.left:
                nextq.append(right_node.left)
            if right_node.right:
                nextq.append(right_node.right)

            right_view.append(right_node.val)
        
        return right_view
    
    '''
    need to find right most element at each level -> traverse through tree by level -> BFS
    '''