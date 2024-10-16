from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # keep track of # of valid subarrays and total sum of current subarray
        count = 0
        total_sum = 0
        # find the total sum of the first subarray -> O(k)
        for z in range(k-1):
            total_sum += arr[z]
        
        i, j = 0, k - 1
        while j < len(arr):
            # update to the next subarray
            total_sum += arr[j]
            
            # check if current subarray is valid
            average = total_sum / k
            if average >= threshold:
                count += 1

            # update to the next subarray
            total_sum -= arr[i]
            i += 1
            j += 1
        
        return count

    '''
    find the # of subarrays of size k with average greater than or equal to threshold
    subarrays -> sliding window

    keep track of the # of subarrays that satisfy the condition
    initialize i, j = 0, k - 1
    the first subarray of size k starts at index 0
        - find average by summing up contents and dividing by k
        - if average >= threshold then increment count by 1
    increment both i and j by 1 to get the next subarray of size k
        - new_total = old_total - arr[i] + arr[j]
    '''
        