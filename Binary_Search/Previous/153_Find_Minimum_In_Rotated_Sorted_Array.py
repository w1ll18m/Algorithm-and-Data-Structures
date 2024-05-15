class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        start = 0
        end = len(nums) - 1

        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]
        
        while start <= end:
            middle = (start + end) // 2

            if nums[start] <= nums[middle] <= nums[end]:
                return nums[start]
            elif nums[middle] < nums[start]:
                if nums[middle - 1] < nums[middle]:
                    end = middle - 1
                else:
                    return nums[middle]
            elif nums[middle] > nums[end]:
                if nums[middle + 1] > nums[middle]:
                    start = middle + 1
                else:
                    return nums[middle + 1]
        
        return -1

        '''
        sorted array in increasing order -> use binary search
        perform the modified binary search:
        - start = 0 and end = len(nums) - 1
        - middle = (start + end) // 2
        - if nums[middle] < nums[start] then we know that the start of the sequence is between start and middle -> end = middle - 1
        - elif nums[middle] > nums[end] then we know that the start of the sequence is between middle and end -> start = middle + 1
        - we have unique elements so after we check nums[middle] then we must check (middle - 1) or (middle + 1) before setting end or start
        '''