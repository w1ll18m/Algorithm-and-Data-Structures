from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # sort the array in ascending order
        nums.sort()
        
        longest = 0
        nofoperations = 0

        i, j = 0, 0
        while j < len(nums):
            # check if window is valid
            if nofoperations > k:
                # increment left pointer if window is not valid
                nofoperations -= nums[j] - nums[i]
                i += 1
            
            # process the window (compare it to longest so far)
            longest = max(longest, j - i + 1)

            # increment the window
            j += 1
            if j < len(nums):
                nofoperations += (nums[j] - nums[j-1]) * (j - i)
        
        return longest
        
    '''
    operation -> increment an element in nums by 1
    return max possible frequency after performing at most k operations
    
    we can't decrement elements -> consider [2, 4, 1], max freq of 2 is 2 since there are only 2 elements less/equal to 2
    thus we should first sort the array -> [1, 2, 4]
        - to calculate the max frequency of a specific element, only consider elements before it
        - # of operations to convert nums[y] to nums[x] is (nums[x] - nums[y])
    find the longest subarray such that the # of operations to convert all elements to the last element -> sliding window!!!
    
    lets formulate a sliding window solution:
        - valid window: # of operations to convert all elements is less than k
        - keep track of the longest window and the # of operations to convert all elements in current window
        (1) check if window is valid -> check if # of operations < k
        (2) if window is not valid, increment left pointer
            - nofoperations = nofoperations - (nums[j] - nums[i])
            - only once -> we don't need to check subarrays smaller than longest subarray so far
        (3) process the window -> check if j - i + 1 > longest
        (4) increment right pointer
            - last element changes!!!
            - nofoperations = nofoperations + (nums[j] - nums[j-1]) * (j - 1 - i + 1)
                - difference between new last and current last is (nums[j] - nums[j-1])
    thus we visit each element twice so time complexity for a sorted array is O(n)
    however, we need to sort the array first so the true time complexity is O(nlogn)
    '''
        