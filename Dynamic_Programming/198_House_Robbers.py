from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def maxmoney(house):
            if house >= len(nums):
                return 0
            
            # case: rob the house
            if house + 2 in dp:
                rob = nums[house] + dp[house + 2]
            else:
                rob = nums[house] + maxmoney(house + 2)
            
            # case: skip the house
            if house + 1 in dp:
                skip = dp[house + 1]
            else:
                skip = maxmoney(house + 1)
            
            # cache the result in the hashtable
            dp[house] = max(rob, skip)
            return dp[house]
        
        return maxmoney(0)

    '''
    nums -> integer array representing the amount of money in each house
        - can't sort since we need to maintain order of the houses
    it will automatically contact the police if 2 adjacent houses were broken into on the same night
    return the maximum amount of money you can rob without alerting the police

    observe that if we:
        (i) decide to rob house i, then we can't rob house i+1
            - now we need to decide whether to rob house i+2 (recursive!!!)
        (ii) don't rob house i, then we can rob house i+1
            - now we need to decide whether to rob house i+1 (recursive!!!)
    
    thus this looks like a recursive (with memoization) problem -> given house i:
        - base: i >= len(nums) then return 0 since there is no house to rob
        - we can either rob house i or skip house i
            - rob house i -> nums[i] + rob(i + 2)
            - skip house i -> rob(i + 1)
            - we need to take the option that results in the most money -> max(nums[i] + rob(i + 2), rob(i + 1))
        - use hashtable to cache max money for smaller subproblems
    
    thus total time complexity is O(n) since each subproblem is solved at most once
    '''