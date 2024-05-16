import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            ascii_val = ord(task)
            count[ascii_val - 65] += 1

        maxHeap = []
        for i in range(len(count)):
            if count[i] != 0:
                maxHeap.append(count[i] * -1)
        heapq.heapify(maxHeap)

        intervals = 0
        while len(maxHeap) > 0:
            isLastCycle = True
            cycle = [None] * (n + 1)

            i = 0
            while i < n + 1:
                if len(maxHeap) != 0:
                    cycle[i] = heapq.heappop(maxHeap)
                    if cycle[i] < -1:
                        isLastCycle = False
                    i += 1
                    intervals += 1
                else:
                    break
            
            if not isLastCycle:
                intervals = intervals + n + 1 - i

            for i in range(len(cycle)):
                if cycle[i] is None:
                    break
                cycle[i] = cycle[i] + 1
                if cycle[i] != 0:
                    heapq.heappush(maxHeap, cycle[i])

        return intervals
            
    '''
    tasks contains a list of tasks (ex. A A A B B B)
    tasks can be completed in any order but identical tasks must be seperated by at least n intervals
    return the minimum # of intervals required to complete all tasks
    
    assume that there are m tasks to complete
    first step is to create a map to count the number of each tasks -> O(m) time
    [technically we dont need map because there are only 26 letters so we only need an array of length 26]

    we will define a "cycle" as n tasks
    the only way for a cycle to have no cooldown is that there are n + 1 unique tasks
        - if there are not n + 1 unique tasks left then there will be cooling time
        - minimum # of intervals = least # of cycles = maximize cycles with no cooling time
        - for each cycle, take n + 1 unique tasks with the most amount of copies
            - use max heap to keep track of amount of copies
            - pop n + 1 tasks from the heap, subtract 1 from count, and push tasks back on heap if count > 0
    '''