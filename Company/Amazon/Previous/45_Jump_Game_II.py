from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        memoize = [-1 for _ in range(len(nums))]
        # we need 0 jumps to reach the last index if we are already at it
        memoize[len(nums) - 1] = 0

        def min_jumps(i):
            # check if we are at the last index
            if i == len(nums) - 1:
                return 0

            # check if the index hasn't already been processed
            if memoize[i] == -1:
                nofjump = float("inf")
                for j in range(1, nums[i] + 1):
                    # ensure that we don't jump past last index
                    if i + j > len(nums) - 1: break
                    # recurse on subproblem
                    nofjump = min(nofjump, 1 + min_jumps(i + j))
                memoize[i] = nofjump
            
            return memoize[i]
        
        return min_jumps(0)
    
    '''
    nums -> integer array
        - nums[i] represents the max length that you can jump from index i
    return the min # of jumps to reach nums[n-1]

    observe that at each index i, we can reach indices i to i + nums[i] in one jump
    suppose that we knew the minimum # of jumps needed to get from the new index i' > i to the last index
    then min_jumps(i) = min(
                            min_jumps(i + 1),
                            min_jumps(i + 2),
                            ... ,
                            min_jumps(i + nums[i])
                        )
    if i == len(nums) - 1 or i + nums[i] >= len(nums) - 1 then we can reach it in 1 jump

    we have a recursive relation that we can memoize in order to solve this problem in O(n^2) time
    '''