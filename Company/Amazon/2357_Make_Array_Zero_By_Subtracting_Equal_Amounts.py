from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums_set = set(nums)

        nofoperations = len(nums_set)
        if 0 in nums_set:
            nofoperations -= 1 
        
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
    thus observe that the # of observations is the # of unique non-zero elements in the array!!

    convert array into a set and return len(set) [-1 if 0 is in the array] -> O(n) time complexity
    '''