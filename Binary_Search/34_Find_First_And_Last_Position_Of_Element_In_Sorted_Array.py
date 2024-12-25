from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]

        # first binary search to find first occurrence of target
        i, j = 0 , len(nums) - 1
        while i <= j:
            middle = (i + j) // 2
            # if target is found then record it and search left subarray
            if nums[middle] == target:
                result[0] = middle
                j = middle - 1
            # if middle is less than target then search right subarray
            elif nums[middle] < target:
                i = middle + 1
            # if middle is greater than target then search left subarray
            else:
                j = middle - 1
        
        # if target was not found then return [-1, -1]
        if result[0] == -1:
            return result
        
        # second binary search to find second occurrence of target
        i, j = 0 , len(nums) - 1
        while i <= j:
            middle = (i + j) // 2
            # if target is found then record it and search right subarray
            if nums[middle] == target:
                result[1] = middle
                i = middle + 1
            # if middle is less than target then search right subarray
            elif nums[middle] < target:
                i = middle + 1
            # if middle is greater than target then search left subarray
            else:
                j = middle - 1
        
        return result
    
    '''
    nums -> integer array sorted in non-decreasing order -> 2 pointers? binary search?
    find the starting and ending positions of a given target value in O(log n) time -> binary search!!!

    we need to run two instances of binary search -> once to find first occurrence and once to find last occurrence
        - find first occurrence -> if element found then record instance and search left subarray
        - find last occurrence -> if element found then record instance and search right subarray
        - if element is not found in first binary search then return [-1, -1]
    
    thus total time complexity is O(log n) and total space complexity is O(1)
    '''