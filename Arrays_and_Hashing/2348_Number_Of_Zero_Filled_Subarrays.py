from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        longest = 0
        total = 0

        for num in nums:
            if num == 0:
                longest += 1
                total += longest
            else:
                longest = 0
        
        return total
    
    '''
    can do in one pass -> O(n)
    keep track of length of contiguous subarray of 0
    
    [0 0 0] has [0] [0] [0] + [0 0] [0 0] + [0 0 0]
    [0 0 0 0] has [0] [0] [0] [0] + [0 0] [0 0] [0 0] + [0 0 0] [0 0 0] + [0 0 0 0]

    thus we add the current length of the contiguous subarray to the total count
    since [0] has 1 subarray
    [0 0] has 1 + 2 subarrays (but we already added 1 from before)
    [0 0 0] has 1 + 2 + 3 subarrays (but we already added 1 and 2 from before)
    '''
        