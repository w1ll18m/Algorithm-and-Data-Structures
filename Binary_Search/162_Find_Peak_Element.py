from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            middle = (i + j) // 2
            # check if middle element is a peak
            if (middle == 0 or nums[middle] > nums[middle - 1]) and (middle == len(nums) - 1 or nums[middle] > nums[middle + 1]):
                return middle
            # recurse on the subarray with the greater neighbour
            elif middle > 0 and nums[middle - 1] > nums[middle]:
                j = middle - 1
            else:
                i = middle + 1
                
    '''
    peak element -> element that is strictly greater than its neighbours
    find a peak element in an integer array in O(log n) time -> binary search?

    the only arrays without peaks (not at the end) are the arrays that are strictly increasing/decreasing
    if an array is not strictly increasing/decreasing then it must have a peak not at the ends

    lets consider the middle element ((i + j) // 2) then
        - if neighbours are strictly less than middle then we found the peak
        - recurse on the subarray with the greater neighbour
            - if the subarray is not strictly increasing/decreasing then it must have a peak
            - if the subarray is strictly increasing then j must be a peak (j is either the end or j + 1 is smaller)
                - if we only recurse on the side with the greater neighbour then j must be the greater neighbour
            - if the subarray is strictly decreasing then middle + 1 must be a peak
    
    thus total time complexity is O(log n) and total space complexity is O(1) since we are performing modified binary search
    '''