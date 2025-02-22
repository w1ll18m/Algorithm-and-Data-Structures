from typing import List
from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        # push n elements to the min heap -> O(nlogk) time complexity
        kmin = []
        for key, value in count.items():
            # push the current item to the heap -> O(logk)
            heapq.heappush(kmin, (value, key))
            # pop the smallest item in the heap if its full -> O(logk)
            if len(kmin) > k:
                heapq.heappop(kmin)

        # pop k elements from the min heap -> O(klogk) time complexity
        most_frequent = []
        for count, num in kmin:
            most_frequent.append(num)
        
        return most_frequent
    
    '''
    nums -> integer array
    return the k most frequent elements -> heap?

    count the # of elements (store in hashmap) -> O(n) time complexity 

    what if we maintained a max heap and popped k elements?
        - heap of size n so O(logn) push/pop 
        - thus pushing n elements will result in O(nlogn) time complexity
    
    what if we maintained a min heap of the k greatest elements?
        - the smallest element in the heap is the smallest of the k greatest elements
        - push the current element into the heap -> pop the smallest element in the heap
        - heap of size k so O(logk) push/pop
        - thus pushing n elements will result in O(nlogk) time complexity
    '''