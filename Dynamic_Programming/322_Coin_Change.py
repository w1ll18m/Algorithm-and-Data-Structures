from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # intialize the array for memoization
        dp = [-1 for _ in range(amount + 1)]

        def findMinCoins(target):
            # if target is 0 then no coins are needed
            if target == 0:
                return 0
            # check if subproblem has already been computed
            elif dp[target] != -1:
                return dp[target]
            
            min_coins = float("inf")
            for coin in coins:
                # if coin is less than target then check how many coins is needed to make target - coin
                if coin <= target:
                    nofcoins = 1 + findMinCoins(target - coin)
                    # take the coin that results in the fewest number of coins needed to make target - coin
                    min_coins = min(min_coins, nofcoins)

            # memoize
            dp[target] = min_coins
            return dp[target]
        
        least_coins = findMinCoins(amount)
        if least_coins < float("inf"):
            return least_coins
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
    
    observe that given the coins array and a target:
        - if target == 0 then no coins needed so return 0
        - if coins[i] <= target and we take coins[i] then we need to find the fewest number of coins that make up target - coins[i]
            - RECURSIVE SUBPROBLEM!!!
        - thus we should take the coin that results in the fewest number of coins for the new subproblem
    we can use memoization to keep track of results for subproblems (targets less than amount) 

    thus total time complexity is O(n * m) where n is the # of coins and m is amount
    and total space complexity is O(m) to keep track of the results of subproblems for memoization
    '''