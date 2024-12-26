class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        start = 0
        end = len(nums) - 1

        while start <= end:
            middle = (start + end) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < nums[start]:
                if nums[middle] < target <= nums[end]:
                    start = middle + 1
                else:
                    end = middle - 1
            elif nums[middle] > nums[end]:
                if nums[start] <= target < nums[middle]:
                    end = middle - 1
                else:
                    start = middle + 1
            else:
                if nums[middle] < target:
                    start = middle + 1
                else:
                    end = middle - 1
        
        return -1

        '''
        middle = (start + end) // 2
        case 1: nums[middle] < nums[start] then min is on the left side -> the right side is sorted
        case 2: nums[middle] > nums[end] then min is on the right side -> the left side is sorted
        case 3: nums[start] <= nums[middle] <= nums[end] then the entire array is sorted
            - becomes normal binarys search
        case 4: nums[middle] = target then return the index

        for case 1 do the following to look for the target:
            - since the right side is sorted check if the target is between nums[middle] and nums[end]
            - if the target is in that range then let start = middle + 1 and search the right side
            - otherwise search the left side so let end = middle - 1
        for case 2 do the following to look for the target:
            - since the right side is sorted check if the target is between nums[start] and nums[middle]
            - if the target is in that range then let end = middle - 1 and search the left side
            - otherwise search the right side so let start - middle + 1
        '''
                