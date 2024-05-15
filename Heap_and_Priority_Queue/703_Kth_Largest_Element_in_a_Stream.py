import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = nums
        heapq.heapify(self.minheap)

        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]

    '''
    kth largest element -> consider using some kind of heap (min or max)
    observe that we only care about the kth largest element so we don't care about any elements before l

    how can we return the kth largest element in O(log k))?
    attempt 1 -> use a max heap of size k
    - but returning the kth greatest would take O(k log k)

    attempt 2 -> use a min heap of size k but only include the greatest elements
    - if we add an element less than kth greatest then nothing changes
    - if we add an element greater than kth greatest then kth greatest becomes k+1st greatest
        - pop from heap and insert new element
    note that attempt 2 is incorrect because we did not consider the case where the initial stream has less than k elements

    attempt 3 -> same as attempt 2 but we add all elements to the heap but pop if there are more than k elements
    '''