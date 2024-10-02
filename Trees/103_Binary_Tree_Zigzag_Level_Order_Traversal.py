from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelOrder = []
        isToRight = True
        current = []
        next = []

        if root is None:
            return current
        current.append(root)

        # if current level is not empty, then append nodes to solution array
        while len(current) != 0:
            # stacks are lists -> iterate from end of list to beginning (preserves order of current stack)
            for i in range(len(current) - 1, -1, -1):
                # append children of current level node to next level stack
                if isToRight:
                    if current[i].right: next.append(current[i].right)
                    if current[i].left: next.append(current[i].left)
                else:
                    if current[i].left: next.append(current[i].left)
                    if current[i].right: next.append(current[i].right)
                
                current[i] = current[i].val
            
            # append nodes in current level to solution array
            levelOrder.append(current)
            isToRight = not isToRight
            current = next
            next = []
        
        return levelOrder
            
    '''
    return the zigzag level order traversal of tree nodes by alternating:
        - from nodes left to right
        - from nodes right to left

    use boolean to keep track of which direction the level is on
    level order traversal -> use BFS
        - maintain stack containing nodes from current level + stack containing nodes from next level
        - assume that the nodes of the current level stack is in the correct order (bottom is first node in level)
            - the next level should be in reverse order (due to zigzag)
            - aka children of last node of current level should be the first nodes in the next level
            - while current level stack is not empty -> pop node -> add children of node to next level stack
    O(n) time complexity -> we traverse through each node exactly once

    THIS SOLUTION ENSURES THAT EACH NODE IS VISITED EXACTLY ONCE
    IF WE JUST DO NORMAL BFS THEN WE NEED TO PASS THROUGH THE LIST AGAIN TO REVERSE IT
    '''