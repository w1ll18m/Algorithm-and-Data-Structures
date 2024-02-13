class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left = [None] * len(nums)       # left[i] is the product of all numbers left of i
        right = [None] * len(nums)      # right[i] is the product of all numbers right of i

        left[0] = 1                     # there is no number left of the first element
        right[len(nums) - 1] = 1        # there is no number right of the last element

        # calculate left and right products
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        
        answer = [None] * len(nums)
        for i in range(0, len(nums)):
            answer[i] = left[i] * right[i]
        
        return answer

        # hint: observe that nums[i] can be calculated by multiplying its left product and right product
        