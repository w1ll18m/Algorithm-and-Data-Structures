class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # edge case where array is empty
        if len(nums) == 0:
            return 0

        numdict = {}

        # initialize the dictionary containing the numbers
        for i in range(0, len(nums)):
            numdict[nums[i]] = i

        longest_sequence = 1                                # keep track of length of longest sequence
        for i in range(0, len(nums)):                       
            current_sequence = 1                            # reset length if current sequence to 1

            if nums[i] not in numdict:                      # if number not in dictionary then it is already used in discovered sequence (no need to check)
                continue

            upper = nums[i] + 1             
            while upper in numdict:                         # check if n+1 is in the array
                del numdict[upper]                          # delete number from dictionary so it is not checked again (not O(n) time otherwise)
                upper += 1
                current_sequence += 1
            
            lower = nums[i] - 1
            while lower in numdict:                         # check if n-1 is in the array
                del numdict[lower]                          # delete number from dictionary so it is not checked again (not O(n) time otherwise)
                lower -= 1
                current_sequence += 1
            
            if current_sequence > longest_sequence:         # check if length of current sequence is longer than length of longest sequence
                longest_sequence = current_sequence
    
            del numdict[nums[i]]                            # delete number from dictionary so it is not checked again (not O(n) time otherwise)
        
        return longest_sequence

        # tried dp approach -> doesnt work -> can only keep track of 1 sequence at a time
        # hint: observe that we can check if a number exists in O(1) time in a dictionary 
        #       for a given number n, if n+1 or n-1 is in array then there is a sequence
        # pattern: checking if a number exists in an array -> hashing