from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1

        while i <= j:
            middle = (i + j) // 2

            # if middle element is equal to target then return it
            if nums[middle] == target:
                return middle
            # if middle element is greater than start then left subarray is sorted
            elif nums[middle] >= nums[i]:
                # if target is within range of left subarray then search left subarray
                if nums[middle] > target >= nums[i]:
                    j = middle - 1
                # if target is not within range of left subarray then search right subarray
                else:
                    i = middle + 1
            # if middle element is less than end then right subarray is sorted
            else:
                # if target is within range of right subarray then search right subarray
                if nums[middle] < target <= nums[j]:
                    i = middle + 1
                # if target is not within range of right subarray then search left subarray
                else:
                    j = middle - 1
        
        return -1

    '''
    nums -> sorted distinct integer array -> 2 pointers? binary search?
    nums is possibly rotated at an unknown pivot index k 
    return the index of target if it exists in O(log n) time -> binary search

    at each step, examine the middle element ((i + j) // 2) as follows:
        - if the middle element is equal to the target then return it

        - if middle > i then left subarray is sorted
            - if i < target < middle then search left subarray
            - otherwise search right subarray

        - if middle < j then right subarray is sorted
            - if middle < target < j then search right subarray
            - otherwise search left subarray
    
    thus total time complexity is O(log n) since we are performing modified binary search
    '''