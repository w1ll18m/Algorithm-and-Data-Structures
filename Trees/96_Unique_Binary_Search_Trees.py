class Solution:
    def numTrees(self, n: int) -> int:
        # keep track of result of smaller n
        nofunique = [1] * (n + 1)

        for i in range(1, n + 1):
            num_unique = 0
            # choose a node in the list as the root
            for j in range(1, i + 1):
                # calculate the # of nodes smaller 
                x = j - 1   # there are j nodes from 1 to j
                # calculate the # of nodes greater
                y = i - j   # there are i nodes total but j of them are from 1 to j

                # get the # of structurally unique BSTs that can be made with the subtrees
                left = nofunique[x]
                right = nofunique[y]

                # total # of possible subtree combinations is dfs(x) * dfs(y)
                num_unique += left * right
            nofunique[i] = num_unique

        return nofunique[n]
            
    '''
    lets recursively calculate the number of structurally unique BST
        - choose any node in the list of nodes as the root
        - observe that a binary tree requires smaller values to be on left and bigger values to be on right
            - let x represent the # of nodes smaller and y represent the # of nodes greater
            - recurse on x to get the # of structurally unique BST of the left subtree
            - recurse on y to get the # of structurally unique BST of the right subtree
            - thus total # of possible subtrees is dfs(x) * dfs(y)
        - to get the total #, we need to repeat this process with every node in the list as the root
            - dfs solution is NOT EFFICIENT since we recalculate smaller n multiple times
            - memoization is better since we can save the result of smaller n
    thus the total time complexity is O(n^2)
    '''
        