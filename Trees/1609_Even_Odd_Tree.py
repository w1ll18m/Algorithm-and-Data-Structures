from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        nodes = deque()
        nodes.append(root)
        isEvenLevel = True
        
        while len(nodes) != 0:
            if isEvenLevel:
                prev = float("-inf")
                # check if all nodes in the level follow the conditions
                for i in range(len(nodes)):
                    cur = nodes.popleft()

                    # check if the node is odd
                    if cur.val % 2 != 1: 
                        return False
                    # check if the node is greater than the last node
                    if cur.val <= prev: return False
                    prev = cur.val

                    if cur.left: nodes.append(cur.left)
                    if cur.right: nodes.append(cur.right)
            else:
                prev = float("inf")
                # check if all nodes in the level follow the conditions
                for i in range(len(nodes)):
                    cur = nodes.popleft()

                    # check if the node is even
                    if cur.val % 2 != 0: return False
                    # check if the node is less than the last node
                    if cur.val >= prev: return False
                    prev = cur.val

                    if cur.left: nodes.append(cur.left)
                    if cur.right: nodes.append(cur.right)
            
            # flip after each level
            isEvenLevel = not isEvenLevel
        
        return True
                
    '''
    want to check if each level follows even-odd -> BFS
    keep track if level is odd or even (flip after each level)
    if even level, then check if integers are odd and if integer is greater than the last
    if odd level, then check if integers are even and if integer is smaller than the last
    thus O(n) time complexity and O(n) space complexity
    '''
        