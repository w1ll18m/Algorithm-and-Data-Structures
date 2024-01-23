class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        lofcost = len(cost)
        M = [None] * (lofcost + 1)
        M[0] = 0
        M[1] = cost[0]

        for i in range(2, lofcost + 1):
            M[i] = min(M[i-1], M[i-2]) + cost[i-1]

        return min(M[lofcost], M[lofcost-1])    # top of the stair can be reached through 1 step from nth step or through 2 steps from n-1th step

        # let M[i] be the min cost of climbing i steps
        # M[0] = 0, M[1] = cost[0], M[i] = min(M[i-1], M[i-2]) + cost[i-1]