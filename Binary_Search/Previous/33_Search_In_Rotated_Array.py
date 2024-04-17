class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        start = 0
        end = len(nums) - 1
        minindex = -1

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        while start <= end:
            middle = (start + end) // 2

            if nums[start] <= nums[middle] <= nums[end]:
                minindex = start
                break
            elif nums[middle] > nums[end]:
                start = middle + 1
            else:
                end = middle
        
        sorted_array = nums[minindex:] + nums[:minindex]
        print(sorted_array)

        start = 0
        end = len(sorted_array) - 1

        while start <= end:
            middle = (start + end) // 2

            if sorted_array[middle] == target:
                return (middle + minindex) % (len(nums))
            elif sorted_array[middle] < target:
                start = middle + 1
            else:
                end = middle -1
        
        return -1
                