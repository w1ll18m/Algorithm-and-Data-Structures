class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] > target:         # if sum > target then next smallest sum can be obtained by moving right pointer
                right -= 1
            else:                                               # if sum < target then next biggest sum can be obtained by moving left pointer
                left += 1
        