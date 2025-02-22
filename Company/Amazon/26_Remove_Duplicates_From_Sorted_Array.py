from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # keep track of previous element
        prev = -200
        # keep track of index of next unique element
        i = 0

        # iterate through the array looking for unique elements
        for j in range(len(nums)):
            # if element is different than the previous element then it is unique
            if nums[j] != prev:
                # move the unique element to index i
                nums[i] = nums[j]
                # increment index i
                i += 1
            
            # set the previous element
            prev = nums[j]

        # i also represents the # of unique elements
        return i
    
    '''
    nums -> sorted in non-decreasing order
    remove duplicates in-place such that each unique element appears only once

    iterate through the array -> unique element encountered when its different than the previous element
    need to maintain two pointers -> point to index of next unique element + point to index of next element
        - swap elements at pointers when we encounter a unique element -> O(1)
        - increment both pointers

    thus total time complexity is O(n) and total space complexity is O(1)
    '''