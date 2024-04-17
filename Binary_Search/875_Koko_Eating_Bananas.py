class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        start = 1
        end = 0
        for i in range(len(piles)):
            end = max(end, piles[i])

        while start < end:
            middle = (start + end) // 2

            total_h = 0
            for i in range(len(piles)):
                total_h += piles[i] / middle
                if piles[i] % middle != 0:
                    total_h += 1
            
            if total_h > h:
                start = middle + 1
            elif total_h <= h:
                end = middle
        
        return start

        '''
        denote the maximum pile of bananas as size m then observe that k must be between 1 and m
            - we can find this in O(n) time

        brute force approach would be to iterate from 1 to m and calculate # of hours 
            - calculating the # of hours would take O(n) time since we would just take the ceiling of piles[i] / k
            - thus the total time complexity of this solution would be O(m * n)

        observe that we can use a modified binary search in order to reduce search space
            - middle = (start + end) // 2
            - calculate the number of hours that it takes eating k = middle banana an hour -> O(n) time
            - case 1: h' > h then k is too small so search to the right of middle
              case 2: h' < h then k is too big so search to the left of middle
                - consider edge case where k + 1 results in h + 1 instead of h thus we must consider middle too
              case 3: h' = h then k is either too big or the min so search to the left of middle (inclusive)
            - thus the total time complexity of this solution would be O(log(m) * n)
        '''


        