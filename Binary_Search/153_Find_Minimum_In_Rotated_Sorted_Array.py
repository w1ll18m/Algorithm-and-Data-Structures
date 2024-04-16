class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        start = 0
        end = len(nums) - 1

        # observe that the minimum element will always be between nums[start] and nums[end]
        while start <= end:
            middle = (start + end) // 2

            if nums[start] <= nums[middle] <= nums[end]:            # nums[start] is smaller than all other elements thus it must be the min element
                return nums[start]
            elif nums[middle] > nums[end]:                          # min element is on right of middle (middle can't be min)
                start = middle + 1
            else:                                                   # nums[middle] < nums[start]
                end = middle                                        # min element is on left of middle (middle can potentially be min)
                                                                    # note that end = middle is safe here
