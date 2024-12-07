from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # sort the array
        nums.sort()
        
        min_score = float('inf')
        i, j = 0, k - 1
        # compute the difference of each window of size k in the sorted array
        while j < len(nums):
            diff = nums[j] - nums[i]
            min_score = min(min_score, diff)
            i, j = i + 1, j + 1
        
        return min_score

    '''
    nums[i] represents the score of the ith student
    pick the scores of any k students -> highest and lowest of k scores is minimized
    (choose a group of k elements such that the difference between the highest and lowest value is minimized)

    to minimize difference, the k scores need to be as close to each other as possible -> sort the array -> O(nlogn)
    check all group of k consecutive scores -> fixed sliding window -> O(n)
        - let i and j point to the start and end of the window respectiviely
        - difference is just sorted[j] (highest) - sorted[i] (lowest)
    thus total time complexity is O(nlogn) and total space complexity is O(1)
    '''