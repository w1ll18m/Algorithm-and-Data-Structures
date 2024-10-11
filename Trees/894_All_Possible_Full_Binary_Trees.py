from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # initialize results array from 0 to n
        count = [None] * (n + 1)
        for i in range(len(count)):
            count[i] = []
        # if n == 1 then we can create exactly 1 full binary tree
        count[1] = [TreeNode(0, None, None)]

        # iteratively calculate full binary trees with 2 to n nodes
        for i in range(2, n + 1):
            # one node needs to be the root thus we have n-1 nodes to distribute to subtrees
            nofnodes = i - 1

            # find left and right subtrees when # of nodes ranges from 1 to i - 2 
            for j in range(1, nofnodes):
                nofleft = j
                # if left subtree has j nodes then right subtree has (nofnodes - j) nodes
                nofright = nofnodes - j

                # recurse on x, y then dfs(x) * dfs(y) to form all possible full binary trees for pair (x,y)
                left_trees = count[nofleft]
                right_trees = count[nofright]
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(0, left_tree, right_tree)
                        # add the full binary tree with i nodes to the results array
                        count[i].append(root)
        
        return count[n]

    '''
    lets recursively calculate the total # of full binary trees:
        - if n == 1 then we can create exactly 1 fully binary tree
        - if n > 1 then:
            - 1 node needs to be the root thus we have n-1 nodes to distribute to subtrees
            - let x, y > 0 be all pairs such that x + y = n - 1 
                - (1, n-2), (2, n-3), (3, n-4), ...
                - left subtree will have x nodes and right subtree will have y nodes
            - recurse on x, y then dfs(x) * dfs(y) is the # of possible full binary trees for pair (x,y)
                - if it is not possible to create a full binary tree for the left or right subtree then dfs(x) = 0 or dfs(y) = 0
                    - thus dfs(x) * dfs(y) = 0 which corresponds to how there are no full binary tree for pair (x,y)
    overlapping subproblems -> use memoization to build an efficient bottom-up solution
    time complexity is O(2^n) -> difficult to prove, lots of math!!!
    '''
        