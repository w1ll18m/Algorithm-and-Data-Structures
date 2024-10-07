from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumPaths(node, ancestor):
            # if node is Leaf then (ancestor + node.val) is a root-leaf path
            if node.left is None and node.right is None:
                return ancestor + node.val
            
            # sum up the paths of the left subtree and right subtree
            total_sum = 0
            # if left child is not empty then recurse and pass ((ancestor + node.val) * 10)
            if node.left is not None:
                total_sum += sumPaths(node.left, (ancestor + node.val) * 10)
            # if right child is not empty then recurse and pass ((ancestor + node.val) * 10)
            if node.right is not None:
                total_sum += sumPaths(node.right, (ancestor + node.val) * 10)
            
            return total_sum
        
        return sumPaths(root, 0)

    '''
    return the total sum of all root-to-leaf numbers
    
    we want to traverse a path completely before moving on to the next -> DFS
    solve with recursive solution, given a node:
        - if node is None then return 0
        - if node is Leaf then return value
        - if node is Not Leaf:
            - if node has both children then return [value + dfs(left)), value + dfs(right)]
            - if node has only left child then return [value + dfs(left)]
            - if node has only right child then return [value + dfs(right)]
    since we are visiting n nodes and we are adding value to possible n strings then time complexity is O(n^2) 

    however, we can actually improve this time complexity significantly
    instead of returning a list of values, return a combined value instead
    at each node, sum up the paths of the left subtree and the right subtree
    keep track of the values of the ancestors of each node 
    solve with recursive solution, given a node:
        - if node is Leaf then return value + ancestor_val
        - if node is not Leaf:
            - if node has both children then return dfs(left) + dfs(right)
            - we pass (value + ancestor_val) * 10 to dfs function
                - allows us to create next digit of the path
    since we are visiting n nodes and we are adding 2 values together then time complexity is O(n)

    THIS IS JUST NORMAL DFS BUT WE PASS EXTRA INFROMATION ABOUT ANCESTOR DURING DFS
    '''