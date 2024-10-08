from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def calculateMax(node):
            # if node is None then return [0, 0] (there is nothing to rob)
            if node is None:
                return [0, 0]
            
            # calculate the max profit of left and right subtrees
            lmax = calculateMax(node.left)
            rmax = calculateMax(node.right)

            # calculate the max profit if we robbed the current node
            rob_max = node.val + lmax[1] + rmax[1]
            # calculate the max profit if we did not rob the current node
            no_rob_max = max(lmax[0], lmax[1]) + max(rmax[0], rmax[1])

            return [rob_max, no_rob_max]
        
        # calculate the max profit if we robbed the root and if we didn't rob the root then return the greater sum
        max_profit = calculateMax(root)
        return max(max_profit[0], max_profit[1])

    '''
    given the root of the binary tree, return the maximum amount of money the thief can rob
    contact police if 2 directly-linked houses were broken into on the same night

    find max value, explore all possibilities -> DP maybe?
        - how can we build a top-down solution?
    lets first attempt a recursive solution:
        - maintain a value that indicates if the parent was robbed 
        - if node is None then return 0
        - case 1: node is robbed then return val + dfs(node.left.left) + dfs(node.left.right) + dfs(node.right.left) + dfs(node.right.right)
        - case 2: node is not robbed then return dfs(node.left) + dfs(node.right)
        - thus if node then return max(val + dfs(node.left.left) + dfs(node.left.right) + dfs(node.right.left) + dfs(node.right.right),
                                       dfs(node.left) + dfs(node.right))
    observe that we can use a hashmap with nodes as the key for memoization but this is O(n) space complexity

    there is a binary decision at each step (rob or not to rob) -> use "return 2 values" approach
    dfs(node) gives us the max value but we dont know if the node is included or not
    we can add this information by returning both the max value if the node is included and if it isn't
    lets build a top-down solution that leverages "return 2 values":
        - if node is None then return [0, 0]
            - first val represents max value if node is included
            - second val represents max value if node is not included
        - case 1: node is robbed then return val + dfs(node.left)[1] + dfs(node.right)[1]
        - case 2: node is not robbed then return max(dfs(node.left)[0], dfs(node.left)[1]) + max(dfs(node.right)[0], dfs(node.right)[1])
        - thus if node then return [val + dfs(node.left)[1] + dfs(node.right)[1],
                                    max(dfs(node.left)[0], dfs(node.left)[1]) + max(dfs(node.right)[0], dfs(node.right)[1])]
    we visit each node exactly once and don't maintain a hashmap thus we have O(n) time complexity and O(1) space complexity
        - space complexity does not account for recursion stack
    '''
        