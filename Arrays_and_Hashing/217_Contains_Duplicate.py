class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        elmcount = {}
        
        for i in range(len(nums)):
            if nums[i] not in elmcount:
                elmcount[nums[i]] = 1
            else:
                return True
        
        return False
    
    # pattern: counting the # of elements -> hashing