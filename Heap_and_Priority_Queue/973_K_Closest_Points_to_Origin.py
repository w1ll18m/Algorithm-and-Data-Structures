import math 
import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        heapq.heapify(minheap)

        for point in points:
            expr1 = point[0] ** 2
            expr2 = point[1] ** 2
            distance = math.sqrt(expr1 + expr2)
            heapq.heappush(minheap, (distance, point))
        
        k_closest = []
        for i in range(k):
            next_closest = heapq.heappop(minheap)
            next_closest_point = next_closest[1]
            k_closest.append(next_closest_point)
        
        return k_closest

    '''
    points[i] represents the ith point on the X-Y plane
    find the kth closest points to the origin (0, 0) -> min heap for distance

    iterate through the array and calculate the distance to the orgin and push it into a heap
    then pop k points from the heap
    '''
        