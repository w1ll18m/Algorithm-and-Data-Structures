# 3005 Count Elements With Maximum Frequency
# Array, Hash Table, Counting

from typing import List
from collections import defaultdict

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        num_max = 0
        count = defaultdict(int)
        nofmaxfreq = 0

        for num in nums:
            count[num] += 1

            if count[num] > num_max:
                num_max = count[num]
                nofmaxfreq = 1
            elif count[num] == num_max:
                nofmaxfreq += 1

        return nofmaxfreq * num_max

    '''
    nums -> array of positive integers
    return the total frequencies of elements in nums
        - all those elements all have the maximum frequency
    
    approach 1: keep track of max frequency and count map
    keep track of max + count map -> O(n) to pass through the array
    pass through the hashmap and add up elements with max freq -> O(n) to pass through map

        num_max = 0
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
            num_max = max(num_max, count[num])
        
        total_freq = 0
        for num, freq in count.items():
            if freq == num_max:
                total_freq += num_max

        return total_freq
    
    -------------------------------------------------------------------------------------------------------

    approach 2: calculate total frequency in 1 pass
    keep track of max + count map + total # of elements with max frequency -> O(n) with 1 pass
    for each element:
        - increment count
        - if count > max then increment max and set total # of elements with max frequency to 1 
        - if count = max then increment total # of elements with max frequency by 1
    total_frequency = total # of elements with max frequency * max
    '''