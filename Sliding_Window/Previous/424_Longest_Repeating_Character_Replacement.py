class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        occurrence = [0] * 26

        def checkCondition():
            most_frequent = 0
            most_frequent_count = occurrence[most_frequent]
            total_count = 0

            for i in range(len(occurrence)):
                total_count += occurrence[i]
                if occurrence[i] > most_frequent_count:
                    most_frequent = i
                    most_frequent_count = occurrence[i]
            
            nofoperations = total_count - most_frequent_count
            if nofoperations > k:
                return False, total_count
            else:
                return True, total_count

        i, j = 0, 0
        while j < len(s):
            letter = ord(s[j]) - ord('A')
            occurrence[letter] += 1

            isValid, length = checkCondition()
            if not isValid:
                if length - 1 > longest:
                    longest = length - 1

                while not checkCondition()[0]:
                    discarded_letter = ord(s[i]) - ord('A')
                    occurrence[discarded_letter] -= 1
                    i += 1

            j += 1
        
        isValid, length = checkCondition()
        if isValid and length > longest:
            longest = length
        elif not isValid and length - 1 > longest:
            longest = length - 1
        
        return longest
    
    '''
    longest substring (with at most k operations) -> sliding window

    maintain an array with indices 0-25 (represents 26 letters in alphabet)
        - each element represents the # of occurrences in the current window
        - iterating through entire array is O(1) time -> fixed 26 elements
        - calculate the character with most occurrences in O(1) time
        - sum up total # of occurences in O(1) time
    
    left pointer is start of window and right pointer is end of window
    in each iteration:
        - increment right pointer by one and update occurrence array
        - check for the following condition:
            - sum up total # of occurrences and find the character with the most occurrences
            - (total #) - (most #) gives the count of all other characters in the window
            - if (total #) - (most #) > k then we must process the window
        - process the window as follows:
            - length of substring is (total #) - 1
            - check if current substring is longer than the longest substring so far
            - decrement the window as follows:
                - move left pointer and decrement occurence array
                - repeat until condition is met
    since we visit each character twice then total time complexity is O(n)
    '''
        