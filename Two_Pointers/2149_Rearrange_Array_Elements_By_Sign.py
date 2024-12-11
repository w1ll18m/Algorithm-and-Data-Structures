from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        results = []
        
        # initialize pointers i and j
        i, j = 0, 0

        for _ in range(len(nums) // 2):
            # find the next positive number
            while nums[i] < 0:
                i += 1
            # append that number to the results array
            results.append(nums[i])
            i += 1
            
            # find the next negative number
            while nums[j] > 0:
                j += 1
            # append that number to the results array
            results.append(nums[j])
            j += 1
        
        return results
        
    '''
    nums is array of integers 
        - equal length
        - equal number of positive and negative integers
    return the rearrangement of nums such that
        - every consecutive pair of integers have opposite signs
        - for integers with same sign, the order in which they appear in nums is preserved
    
    we want to sequentially traverse positive numbers and negative numbers seperately -> 2 pointers
    (1) create a new results array that holds the elements satisfying the conditions
    (2) initialize pointers i and j that point to the first positive and first negative numbers respectively
    (3) for each iteration (n/2 total):
        (i) append nums[i] to results array and move i to next positive number
        (ii) append nums[j] to results array and move i to the next negative number
    thus total time complexity is O(n) since we visit each element at most twice and total space complexity is O(n) for the results array
    '''