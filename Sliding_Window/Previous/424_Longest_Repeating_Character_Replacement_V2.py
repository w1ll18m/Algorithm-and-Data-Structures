class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        occurrence = [0] * 26
        highest_freq = 0
        
        # finds the highest frequency letter in occurence array in O(26) time
        def findHighestFrequency():
            max_freq = 0
            for i in range(len(occurrence)):
                max_freq = max(max_freq, occurrence[i])
            return max_freq

        i, j = 0, 0
        while j < len(s):
            letter = ord(s[j]) - ord('A')
            occurrence[letter] += 1
            highest_freq = max(highest_freq, occurrence[letter])

            # check if window is valid
            while (j - i + 1) - highest_freq > k:
                discard = ord(s[i]) - ord('A')
                occurrence[discard] -= 1
                highest_freq = findHighestFrequency() 
                # increment the left pointer
                i += 1
            
            # process the window
            longest = max(longest, j - i + 1)

            # increment the right pointer
            j += 1
        
        return longest
    
    '''
    longest substring (with at most k operations) -> sliding window

    maintain an array with indices 0-25 (represents 26 letters in alphabet)
        - each element represents the # of occurrences in the current window
        - iterating through entire array is O(1) time -> fixed 26 elements
        - calculate the character with most occurrences in O(1) time
        - sum up total # of occurences in O(1) time
    
    keep track of count of highest frequency letter in window
    left pointer is start of window and right pointer is end of window
    in each iteration:
        - increment right pointer by one and update the occurrence array (update highest frequency if needed)
        - check if window is valid by checking if (total #) - (most #) > k
            - (total #) - (most #) gives the count of all other characters in the window
        - while the window is not valid: (1) increment the left pointer
                                         (2) decrement occurrence[i]
                                         (3) recompute new highest frequency count
        - check if current substring is longer than the longest substring so far
    since we visit each character twice then total time complexity is O(26n)
    '''
        