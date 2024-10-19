from typing import List
from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        longest = 0
        count = defaultdict(int)

        i, j = 0, 0
        while j < len(nums):
            # update the count of the new element
            count[nums[j]] += 1
            
            # check if the window is valid
            if count[nums[j]] > k:
                # increment left pointer until first occurrence of nums[j]
                while nums[i] != nums[j]:
                    # update the count of the removed element
                    count[nums[i]] -= 1
                    i += 1
                # left pointer at first occurrence of nums[j] thus increment to remove it
                count[nums[i]] -= 1
                i += 1
            
            # process the window
            longest = max(longest, j - i + 1)

            # increment right pointer to get the next window
            j += 1
        
        return longest
    
    '''
    frequency of x is the # of times that it occurs in an array
    array is good if frequency of each element is less/equal to k
    find the length of the longest good subarray of nums -> sliding window!!!

    lets formulate a sliding window solution:
        - maintain a hashtable that maps elements to count
        - valid window: each element has frequency of k or less
            - how to check if valid window? -> check if count[nums[j]] <= k
            - how to reduce window? -> increment left pointer until first occurrence of nums[j]
                - balances out the nums[j] that was just added
        - process window: check if j - i + 1 > longest
        - slide window: increment right pointer and increment count
    since we visit each element twice then total time complexity is O(n)
    '''