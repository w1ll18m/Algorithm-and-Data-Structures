from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # initialize the dp array -> O(n) time
        dp = []
        for i in range(len(triangle)):
            # last level should be initialized with dp[i][j] = triangle[i][j]
            if i == len(triangle) - 1:
                row = []
                for j in range(len(triangle[i])):
                    row.append(triangle[i][j])
                dp.append(row)
            else:
                dp.append([-1 for _ in range(len(triangle[i]))])
        
        # compute subproblems bottom-up
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                left_path = dp[i+1][j]
                right_path = dp[i+1][j+1]
                # compute the longest path starting at level i and index j
                dp[i][j] = triangle[i][j] + min(left_path, right_path)
        
        # return the longest path starting at the top (level 0 and index 0)
        return dp[0][0]
                
    '''
    triangle -> array of the format [[0] [1 2] [3 4 5] [6, 7, 8, 9]]
    return the minimum path sum from top to bottom -> DFS to explore all paths

            0
           0 1
          0 1 2 
         0 1 2 3

    observe that each row j has range [0, j)
    then at index j of any given row i, the longest path starting from that node either:
        - triangle[i][j] if current level is the bottom 
        - takes the left path -> triangle[i][j] + minPath(i + 1, j)
        - takes the right path -> traingle[i][j] + minPath(i + 1, j + 1)
        - take the min between both paths
    the total time complexity is O(2^n) since at each node we have two possibilities that we need to explore

    but observe that there are overlapping subproblems -> dp + memoization?
        - ex) triangle[i][j] needs the longest path of triangle[i+1][j+1]
              triangle[i+1][j] need the longest path of triangle[i+1][j+1]
              thus both problems need the results of a common overlapping subproblem
    hence let's intialize dp array [[-1], [-1, -1], [-1, -1, -1]] to store the results of computed subproblems
        - observe that the last level should be intialized with dp[i][j] = triangle[i][j]
        - dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])
    thus total time complexity should be O(n) where n is the # of nodes
    '''