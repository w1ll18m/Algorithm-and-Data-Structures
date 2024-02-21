class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        difference = {}

        for i in range(len(nums)):                      # keep track of complements of every element
            difference[target - nums[i]] = i            # store complement as key and index as value 
        
        for i in range(len(nums)):                      # check if complement exists in the array (if so return current index and stored index)
            if nums[i] in difference:
                if difference[nums[i]] != i:            # each element can only be used once
                    return (i, difference[nums[i]])

        # hint: iterate through array and check if complement (target - current) element exists
        # pattern: checking if a number exists in an array -> hashing

        