from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        sum_weights = 0
        max_weight = 0
        for weight in weights:
            sum_weights += weight
            max_weight = max(max_weight, weight)
        
        def checkShipDays(weight_capacity):
            nofdays = 1

            cur_weight = 0
            i = 0
            while i < len(weights):
                if cur_weight + weights[i] > weight_capacity:
                    nofdays += 1
                    cur_weight = 0

                cur_weight += weights[i]
                i += 1
            
            return nofdays
        
        min_capacity = sum_weights
        i, j = max_weight, sum_weights
        while i <= j:
            middle = (i + j) // 2
            nofdays = checkShipDays(middle)
            
            if nofdays > days:
                i = middle + 1
            else:
                min_capacity = min(min_capacity, middle)
                j = middle - 1
        
        return min_capacity
        
    '''
    weights[i] represents the weight of the ith package
    each day we load weights (in order) onto the ship but not more than the capacity
    what is the minimum weight capacity such that we can ship all the packages within a given number of days -> binary search!!!

    the brute force solution involves trying every possible weight capacity starting from 1
    observe that the maximum weight capacity is the sum of all the weights
        - allows all packages to be shipped in 1 day (any more weight capacity is wasted!!!)
        - takes O(n) time to sum up all integers in the weights array
    observe that the minimum weight capacity is the largest weight
        - otherwise it is not possible to load the weight onto the ship
    thus we can use binary search to find the minimum weight capacity which is between 1 and sum_weights

    lets consider the middle element ((i + j) // 2):
        - check if corresponding weight capacity can be shipped within specified number of days -> O(n)
        - if it needs more than specified number of days then we need more weight capacity so search right side
        - if it needs less than/equal specified number of days then we need less weight capacity so search right side
    note that we need to keep track of smallest valid weight capacity we have seen so far
    thus total time complexity is O(n log m) where m is the sum of weights
    '''