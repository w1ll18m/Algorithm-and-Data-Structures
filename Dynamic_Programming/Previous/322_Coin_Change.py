from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # intialize the 2d array for memoization
        dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins))]

        def minCoins(i, target):
            # if target is 0 then no more coins are needed
            if target == 0:
                return 0
            # if no more coins left then no valid combination exists
            elif i >= len(coins):
                return float("inf")
            # check if subproblem has already been solved
            elif dp[i][target] != -1:
                return dp[i][target]

            min_coins = float("inf")
            # check minimum coin count for all the possiblilities 
            for j in range((target // coins[i]) + 1):
                nofcoins = j + minCoins(i + 1, target - j * coins[i])
                min_coins = min(min_coins, nofcoins)
            
            # memoize
            dp[i][target] = min_coins
            return dp[i][target]
        
        fewest_coins = minCoins(0, amount)
        if fewest_coins < float("inf"):
            return fewest_coins
        else:
            return -1
    
    '''
    coins -> integer array -> sorting?
    return the fewest number of coins that you need to make up that amount

    sort the array in non-increasing order -> O(nlogn)
    what if we used a greedy approach and took at much of the largest denomination possible?
        - ex) [4, 3, 1] with target of 6 
              6 -> 4 + 1 + 1
              6 -> 3 + 3
        - from this example we can see that this does not work
    
    at each index i, we can decide to take up to target // coins[i] copies:
        - if i >= len(coins) and target != 0 then no more coins are left so no valid combination exists -> return float("inf")
        - for j in range(target // coins[i]):
            - we take j copies of the coins[i] so we need to make target - j * coins[i] with the rest of the coins
            - so it takes j + coinChange(i + 1, target - j * coins[i]) coins
            - NOTE: if coins[i] > target then target // coins[i] == 0 so we take 0 copies of that coin
        - take the minimum # of coins in the range
    
    observe that we can use memoization on the recursive relation to avoid resolving subproblems (top-down dp)
    thus total time complexity is O(n * m) where n is the length of coins and m is the target
    '''