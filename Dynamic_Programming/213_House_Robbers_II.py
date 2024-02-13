class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        lofnums = len(nums)
        if lofnums == 1: return nums[0]     # check if theres only 1 house on the street

        M = [None] * (lofnums + 1)
        N = [None] * (lofnums + 1)
        M[0] = 0
        M[1] = nums[0]
        N[0] = N[1] = 0     # first house is not used so N[1] = 0

        for i in range(2, lofnums + 1):
            M[i] = max(M[i-1], M[i-2] + nums[i-1])
            N[i] = max(N[i-1], N[i-2] + nums[i-1])

        return max(M[lofnums - 1], N[lofnums])      # last house is not used so return M[lofnums - 1]
        
        # there are 2 cases: first house is used and first house is not used
        # let M[i] be the max money that can be robbed from the first i houses where first house is used (thus last house is not used)
        #   - should only use nums[0] to nums[n-2]
        # let N[i] be the max money that can be robbed from the first i houses where first house is not used
        #   - should only use nums[1] to nums[n-1]
        # M[i] and N[i] should be calculated the same as regular house robber problem
        