from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # if tree is empty then return empty array
        if root is None:
            return []
        
        row_nodes = deque()
        row_nodes.append(root)
        largest_arr = []
        
        while len(row_nodes) != 0:
            # maintain a variable tracking largest value in row thus far
            largest = (-2) ** 31
            # iterate through nodes in the row
            for i in range(len(row_nodes)):
                node = row_nodes.popleft()
                if node.val > largest: largest = node.val
                # add children of current row node to queue to be processed in next iteration
                if node.left: row_nodes.append(node.left)
                if node.right: row_nodes.append(node.right)
            # add the largest value in the row to the result array
            largest_arr.append(largest)
        
        return largest_arr
    
    '''
    find largest value in each tree row -> BFS
    in each row iteration, maintain a variable tracking the largest value in the row thus far
    since we visit each node exactly once, we have O(n) time complexity
    '''
        