from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total_duration = 0
        prev_end = 0
        for i in range(len(timeSeries)):
            cur_end = timeSeries[i] + duration - 1
            total_duration += duration

            if i != 0 and timeSeries[i] <= prev_end:
                wasted_duration = prev_end - timeSeries[i] + 1
                total_duration -= wasted_duration
            
            prev_end = cur_end
        return total_duration
    
    '''
    ashe gets poisoned for duration seconds
    attack at time t means poisoned for [t, t + duration - 1]
    if teemo attacks again before poison effect ends, time is reset

    timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i]
    '''
        