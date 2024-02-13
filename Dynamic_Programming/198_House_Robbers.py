class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        lofnums = len(nums)
        MaxMoney = [None] * (lofnums + 1)
        MaxMoney[0] = 0
        MaxMoney[1] = nums[0]

        for i in range(2, lofnums + 1):
            MaxMoney[i] = max(MaxMoney[i-1], MaxMoney[i-2] + nums[i-1])
        
        return MaxMoney[lofnums]

    # let i be the number of houses
    # let M[i] be the max amount of money to be stolen from the first i houses
    # then M[0] = 0, M[1] = nums[0], M[i] = max(M[i-1], M[i-2] + nums[i])