import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        k_frequent = []

        elmcount = {}
        for i in range(len(nums)):                          # count the number of elements in the array -> O(n)
            if nums[i] not in elmcount:
                elmcount[nums[i]] = 1
            else:
                elmcount[nums[i]] += 1
        
        elmcountheap = []
        for key, value in elmcount.items():                 # create an array of tuples consisting of the element as the value and the count as the key (multiply count by -1 for max heap) -> O(n)
            elmcountheap.append((value * -1, key))          
        
        heapq.heapify(elmcountheap)                         # O(n) time
        while len(elmcountheap) > 0 and k > 0:              # pop k times from the heap to get the k most frequent elements
            next_frequent = heapq.heappop(elmcountheap)
            k_frequent.append(next_frequent[1])
            k -= 1
        
        return k_frequent
    
    # hint: a max heap can created by multiplying the key by -1
    # pattern: counting the # of elements -> hashing     
    #          return k most frequent elements -> heap        


        
        
                
        