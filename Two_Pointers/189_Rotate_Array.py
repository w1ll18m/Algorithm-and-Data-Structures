from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # calculate the # of rotations using remainder technique 
        rotations = k % len(nums)

        # if no rotations are needed then do nothing and return
        if rotations == 0:
            return

        # define in-place reverse function using 2 pointers
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j - 1
        
        # reverse the entire array
        reverse(0, len(nums) - 1)
        # reverse the first k elements in the modified array
        reverse(0, rotations - 1)
        # reverse the remaining elements in the modified array
        reverse(rotations, len(nums)- 1)
    
    '''
    nums -> array of ints
    rotate the array to the right by k steps

    observe that if k % n == 0 then the array remains the same
    observe that if k % n == 1 then the array is rotated so nums[n] is the head
    observe that if k % n == 2 then the array is rotated so nums[n - 1] is the head
    so if k % n == m then the array is rotated so nums[n - m + 1] is the head

    Reversal Algorithm for Array Rotation:
    (1) assume that we want to rotate an array by k positions
        ex) [1, 2, 3, 4, 5] -> [4, 5, 1, 2, 3] where k = 2

    (2) reverse the entire array
        ex) [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]
        - we want the last k elements to be the first k elements!!!

    (3) reverse the first k elements and the remaining elements
        ex) [4, 5] + [1, 2, 3] -> [4, 5, 1, 2, 3]
        - reverse subarrays independently to achieve original ordering
    
    thus total time complexity is O(n) to perform 3 reverses in-place and total space complexity is O(1)
    '''