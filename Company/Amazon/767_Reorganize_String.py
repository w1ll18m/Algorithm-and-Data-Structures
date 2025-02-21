from collections import defaultdict
import math

class Solution:
    # finds the character (that isnt blacklist) with the greatest count
    def find_most_frequent(self, count, blacklist):
        # keep track of largest key and value so far
        largest_key, largest_value = -1, -1

        for key, value in count.items():
            if key != blacklist and value > largest_value:
                largest_key = key
                largest_value = value
        
        return largest_key

    def reorganizeString(self, s: str) -> str:
        # build the count hashmap
        count = defaultdict(int)
        for char in s:
            count[char] += 1
        
        # check if there is character with count more than ceil(n/2)
        if count[self.find_most_frequent(count, '')] > math.ceil(len(s) / 2):
            return ""
        
        result = ""     # keep track of the result string
        prev = ''       # keep track of the previous character in the string

        for _ in range(len(s)):
            # find the most frequent character that is different from the previous character
            freq_char = self.find_most_frequent(count, prev)
            # append that character to the result string
            result += freq_char
            # decrement the count of that character
            count[freq_char] -= 1
            # set the previous character to that character
            prev = freq_char
        
        return result
 
    '''
    string s -> rearrange the characters of s so that any 2 adjacent characters are not the same

    aaabbc -> ababac (a -> 3, total -> 6, sol)
    aabbcc -> abcabc (a -> 2, total -> 6, sol)
    aaaabcc -> ababaca (a -> 4, total -> 7, sol)
    aaaaabcc -> ababacaa (a -> 5, total -> 8, no sol)

    observe that if is no character with count more than ceil(n/2) then there is a solution

    how do we come up with the solution?
        - keep track of count every single character -> O(n) to build
        - choose character with highest count to be first character
            - O(26) since there are only 26 letters
        - recursively (or iteratively) build rest of string the same way (given that it doesnt start with the chosen character) -> O(n)

    thus total time complexity is O(n) and total space complexity is O(1) since there are only 26 letters

    NOTE: a possible improvement is to use a heap to keep track of largest count instead -> O(log k) pop/push but k is less than 26 thus O(1) pop/push
    '''