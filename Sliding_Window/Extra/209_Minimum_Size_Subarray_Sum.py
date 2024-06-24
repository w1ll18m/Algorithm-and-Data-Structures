from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        i, j = 0, 0 
        cur_sum = 0

        while i < len(nums) and j < len(nums):
            cur_sum = cur_sum + nums[j]
            
            # process the window if sum is greater than the target
            if cur_sum >= target:

                # check if size of window is less than min so far
                min_len = min(min_len, j - i + 1)

                # move i towards j until sum of window is less than target
                while i < j:
                    cur_sum -= nums[i]
                    i += 1
                    if cur_sum >= target:
                        min_len = min(min_len, j - i + 1)
                    else:
                        break
                
                # case where single element is greater/equal than target
                if i == j and cur_sum >= target:
                    return 1
            
            j += 1
        
        if min_len < float('inf'):
            return min_len
        return 0

'''
find min length of subarray whose sum is greater than or equal to target
1. maintain 2 points i and j which represent the window size
2. for each iteration of the while loop:
    a. if the sum is greater/equal to target then process the window
    b. if the sum is less than the target then increment j
3. processing the window:
    a. check if the size of the window is less than min so far
    b. move i towards j until sum of window is less than target
since each pointer i and j visits each element once then total runtime is O(n)
'''