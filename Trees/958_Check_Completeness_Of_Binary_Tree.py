from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        current = [root]
        next = []
        isLastLevel = False

        while len(current) != 0:
            for i in range(0, len(current)):
                if current[i].left: 
                    # child exists but encountered child that is None already -> return False (not far left)
                    if isLastLevel:
                        return False
                    next.append(current[i].left)
                # child does not exist so next level is the last level
                else:
                    isLastLevel = True
                
                if current[i].right: 
                    # child exists but encountered child that is None already -> return False (not far left)
                    if isLastLevel:
                        return False
                    next.append(current[i].right)
                # child does not exist so next level is the last level
                else:
                    isLastLevel = True

            # process the next level
            current = next
            next = []
        
        return True
    
    '''
    complete binary tree -> every level except the last is completely filled

    checking nodes by level -> bfs
    how to know if next level is last level? -> child of a node in current level is None
        - use boolean to keep track if next level is the last level
        - set boolean to True if we encounter a child that is None
        - if boolean is True and we encounter a child that is not None, then nodes in last level are not as far left as possible

    we visit each node exactly once during BFS -> O(n) time complexity
    '''
        