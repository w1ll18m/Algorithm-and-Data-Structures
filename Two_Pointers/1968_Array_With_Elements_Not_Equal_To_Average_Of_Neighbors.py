from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # sort the array
        nums.sort()
        
        # rearrange the array as ABABAB
        results = []
        i, j = 0, len(nums) - 1
        while i < j:
            results.append(nums[i])
            results.append(nums[j])
            i, j = i + 1, j - 1
        
        if len(nums) % 2 != 0:
            results.append(nums[i])
        
        return results

    '''
    nums -> array of distinct integers -> sort?
    rearrange the elements such that nums[i] != (nums[i-1] + nums[i+1]) / 2
    
    observe that if (i) nums[i-1] < nums[i] and nums[i+1] < nums[i] (aka both neighbours are smaller)
                    (ii) nums[i-1] > nums[i] and nums[i+1] > nums[i] (aka both neighbours are larger)
    then the average of neighbours can not be nums[i]

    so we want to split the integers into two groups
        - group A contains integers less than all integers in group B
        - group B contains integers greater than all integers in group A
    thus sort the integers and let [0, n/2] be group A and [n/2 + 1, n] be group B -> O(n * log n)
    
    we want to rearrange the array as A B A B[...] A B A B
    thus total time complexity is O(nlogn) for sorting and total space complexity is O(n)
    '''