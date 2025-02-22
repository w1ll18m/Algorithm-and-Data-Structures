from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        # append each element to the corresponding bucket (each bucket represents a count)
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, value in count.items():
            buckets[value].append(key)
        
        # iterate from largest bucket to smallest
        result = []
        for i in range(len(nums), -1, -1):
            # add nums in current bucket to the result array
            for j in range(len(buckets[i])):
                result.append(buckets[i][j])
                if len(result) == k:
                    return result

    '''
    nums -> integer array
    return the k most frequent elements -> heap?
    observe that count is constrained between [0, n] -> bucket sort!!!

    count the # of elements (store in hashmap) -> O(n) time complexity 
    iterate through the count map and append each element to appropriate bucket -> O(n) time complexity
    iterate from largest bucket to smallest and add the first k elements encountered to the result array -> O(n) time complexity

    thus total time complexity is O(n) and total space complexity is O(n)

    NOTE: BUCKET SORT IS GREAT FOR SORTING IN O(N) TIME WHEN ARRAY ELEMENTS ARE CONSTRAINED!!!
    '''