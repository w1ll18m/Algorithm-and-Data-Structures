from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        min_time = 0

        i, j = 0, 1
        while j < len(colors):
            # check if balloons are the same colour
            if colors[i] != colors[j]:
                i = j
            # check if current balloon is smaller than largest balloon so far
            elif neededTime[i] >= neededTime[j]:
                min_time += neededTime[j]
            # check if current balloon is bigger than largest balloon so far
            else:
                min_time += neededTime[i]
                i = j
            
            # increment pointer j to check the next balloon
            j += 1
        
        return min_time

    '''
    colors[i] represents the ith balloon in rope -> array of characters representing colours
    neededTime[i] represents time needed to remove ith balloon from rope -> array of integers
    consecutive baloons can not be the same colour 

    find the minimum time bob needs to make the rope colourful
    observe that we want to maintain the order of the rope -> no sorting!!!
    observe that given x consecutive balloons of the same colour:
        - we need to remove x - 1 balloons to ensure that the rope is colourful
        - keep the balloon with the largest neededTime[i] to minimize time
    
    thus we want to maintain two pointers i and j:
        - i points to largest  balloon and j points to current balloon
        - if colors[i] == colours[j] then
            (i) if neededTime[i] >= neededTime[j] then remove balloon j 
            (ii) if neededTime[i] < neededTime[j] then remove balloon i and move pointer i
        - if colours[i] != colours[j] then move pointer i
    
    we visit each element at most twice so total time complexity is O(n)
    '''