from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        total_count = 1
        current_count = 1
        current_num = nums[0]

        i, j = 1, 1
        while j < len(nums):
            # check if current num is different from previous num
            if nums[j] != current_num:
                # add current num to the final results array
                nums[i] = nums[j]
                i += 1
                total_count += 1
                # update current num
                current_num = nums[j]
                current_count = 0
            # check if final results array has less than 2 copies of current num
            elif current_count < 2:
                # add current num to the final results array
                nums[i] = nums[j]
                i += 1
                total_count += 1

            current_count += 1
            j += 1
        
        return total_count
    
    '''
    nums -> sorted (non-decreasing) array of ints
    remove duplicates in place such that each unique element appears at most twice -> need a counter

    maintain two pointers i and j
        - i represents the "next" available index in the final result
        - j represents the index of the current element
    need to keep track of total # of elements, total # of current nums, and current num

    (1) if nums[j] != current_num then:
        - nums[i] = nums[j] and i += 1
        - current_num = nums[j] and current_count = 1
    (2) if nums[j] == current_num and current_count < 2 then:
        - nums[i] = nums[j] and i += 1
        - current_count += 1
    (3) if nums[j] == current_num and current_count >= 2 then:
        - current_count += 1
    
    thus we visit each num exactly once so total time complexity is O(n)
    '''