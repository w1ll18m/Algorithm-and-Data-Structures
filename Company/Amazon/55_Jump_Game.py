from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # keep track of the furthest distance that we can reach
        furthest = 0
        for i in range(len(nums)):
            # check if we can reach the last index
            if furthest >= len(nums) - 1:
                return True
            # check if the we can't go any further
            if i > furthest:
                return False
            
            # check if we can reach any further
            furthest = max(furthest, i + nums[i])
    
    '''
    nums -> integer array
        - nums[i] represents the max jump length at the ith index
    return true if you can reach the last index

    observe that at each index i, we can take either 0 to nums[i] jumps
    then we can recursively check if it is possible to make it to the end at the new index i'
    thus the recursive relation becomes canReach(i) = canReach(i + 1) or canReach(i + 2) or ... or canReach(i + nums[i])
    we can use memoization to solve this relation in O(n^2) time

    but we can solve this problem in O(n) time by keeping track of the max distance that we can reach at each step
        - observe that if we can reach index j then we can reach all elements before j too
            - if j >= len(nums) - 1 then we can reach the last index
        - at each index i, the furthest we can reach is i + nums[i]
            - check if i + nums[i] > furthest -> furthest = i + nums[i]
        - iterate through the array until we reach last index or i > furthest (can't go any farther)
    
    thus total time complexity is O(n) and total space complexity is O(1)
    '''