from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            middle = (i + j) // 2
            # right neighbour is equal to middle
            if middle + 1 < len(nums) and nums[middle] == nums[middle + 1]:
                # check if right subarray is odd length
                if (j - (middle + 2) + 1) % 2 == 1:
                    i = middle + 2
                else:
                    j = middle - 1
            # left neighbour is equal to middle
            elif middle - 1 >= 0 and nums[middle] == nums[middle - 1]:
                # check if left subarray is odd length
                if ((middle - 2) - j + 1) % 2 == 1:
                    j = middle - 2
                else:
                    i = middle + 1
            # neighbours are not equal to middle
            else:
                return nums[middle]
    
    '''
    sorted array where every element except one appears exactly twice -> two pointers? binary search?
    return the single element that appears only once in O(log n) time -> binary search

    examine the middle element ((i + j) // 2) then
        - if none of neighbours are equal to middle then we found our target
        - if one of neighbours is equal to middle then we need to recurse on subarray
            - if left neighbour is equal then left subarray is [i, middle - 2]
            - if right neighbour is equal then right subarray is [middle + 2, j]
            - recurse on the subarray with odd length!!!
    '''