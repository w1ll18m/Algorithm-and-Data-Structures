from typing import List

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        totalValues = [0] * len(aliceValues)
        for i in range(len(aliceValues)):
            totalValues[i] = (aliceValues[i] + bobValues[i], i)
        totalValues.sort(reverse=True)
 
        alicePoints = 0
        bobPoints = 0
        for i in range(len(totalValues)):
            stone = totalValues[i][1]
            if i % 2 == 0:
                alicePoints += aliceValues[stone]
            else:
                bobPoints += bobValues[stone]

        if alicePoints < bobPoints:
            return -1
        elif alicePoints > bobPoints:
            return 1
        else:
            return 0

    '''
    n stones in the pile
    each turn -> remove a stone from the pile a recieve points based on value
        - Alice has values aliceValues[i]
        - Bob has values bobValues[i]
    both players will play optimally -> they know each others values

    what does optimal mean?
    the one that gets the most points and takes away the most points too -> choose stone with max(aliceValues[i] + bobValues[i])
    '''
        