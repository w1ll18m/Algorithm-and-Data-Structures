from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # sort the number array
        nums.sort()

        # keep track of # of operations and total subtracted so far
        nofoperations = 0
        total_subtracted = 0

        for i in range(len(nums)):
            # subtract the total amount so far
            nums[i] -= total_subtracted

            # if element is still not zero then add leftover amount and increment operation count
            if nums[i] > 0:
                nofoperations += 1
                total_subtracted += nums[i]
        
        return nofoperations
    
    '''
    nums -> non-negative integer array
        - choose a positive integer x such that x <= smallest in nums
        - subtract x from every positive element in nums
    return the min # of operations to make every element in nums equal to 0

    [1, 5, 0, 3, 5] -> [0, 1, 3, 5, 5]
    choose x = 1 -> [0, 0, 3, 5, 5]
    choose x = 3 -> [0, 0, 0, 2, 2]
    choose x = 2 -> [0, 0, 0, 0, 0]

    why would we choose a value of x that is not equal to the smallest non-zero element? -> no reason at all!!!

    thus we want to 
    (1) sort the array from smallest to largest -> O(nlogn) 
    (2) keep track of total amount subtracted so far
    (3) for each non-zero element:
        - subtract the total amount so far
        - if element is non-zero, add leftover amount to total amount so far and increment operation count
        - move to the next element

    thus total time complexity is O(nlogn) and total space complexity is O(1)
    '''