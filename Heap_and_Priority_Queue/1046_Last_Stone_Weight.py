import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        heapq.heapify(stones)

        for stone in stones:
            heapq.heappush(maxheap, -1 * stone)
        
        while len(maxheap) > 1:
            y = -1 * heapq.heappop(maxheap)
            x = -1 * heapq.heappop(maxheap)

            if y > x:
                new_stone = y - x
                heapq.heappush(maxheap, -1 * new_stone)
        
        if len(maxheap) == 0:
            return 0
        return -1 * maxheap[0]
    
    '''
    stones[i] is weight of the ith stone
    choose the heaviest 2 stones -> consider using heap
    if x == y then stones are destroyed
    if x != y then stone x is destroyed and stone y has new weight y - x

    use max heap to keep track of the heaviest stones (multiply all weights by -1 for max heap)
    1. add all stone weights to the heap
    2. while there is more than one stone in the heap:
        - pop the 2 largest stones off the heap
        - smash them together then add it back into the heap
    '''
        