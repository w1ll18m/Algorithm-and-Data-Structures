from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        results = []
        # sort the interval array by start time
        intervals.sort(key=lambda x: x[0])
        cur = intervals[0]

        for j in range(1, len(intervals)):
            # if interval j does not overlap with interval i then output interval i
            if intervals[j][0] > cur[1]:
                results.append(cur)
                # set interval j as the current interval
                cur = intervals[j]
            # if interval j overlaps with interval i then determine the combined interval
            else:
                cur[1] = max(cur[1], intervals[j][1])
        
        # add the last interval to the results array
        results.append(cur)

        return results
    
    '''
    intervals -> array of intervals
        - interval = [start, end]
    merge all overlapping intervals and return an array of non-overlapping intervals

    how do we know if interval A and interval B overlaps? -> a_start < b_start < a_end OR b_start < a_start < a_end
    what if sorted the intervals by their start? 
        - [[1,3],[2,6],[8,10],[15,18]]
        - observe that given intervals i and j where i = j + 1 (consecutive) and i_start > j_start, there are 2 possibilities:
            (1) j_start > i_end so interval j starts after interval i
                - then interval i is non-overlapping with j (and all other intervals after since intervals are sorted by start time)
            (2) j_start <= i_end so interval j overlaps with interval i
                - the interval that contains both j and i is [i_start, max(i_end, j_end)]
        - what about the case where i_start = j_start?
            - then there is definitely overlap and we should take the interval with greater end time

    thus we should implement the following algorithm
    (1) sort the interval array by start time in non-descending order -> O(nlogn)
    (2) keep track of the current considered interval
    (3) for each subsequent interval, (i) if overlap with current interval -> update current interval
                                      (ii) if no overlap with current interval -> add current interval to result and let subsequent interval be the current interval
    (4) add the current interval at the end of the loop to the results array

    thus we visit each interval exactly once but we require one sort thus total time complexity is O(nlogn)
    '''