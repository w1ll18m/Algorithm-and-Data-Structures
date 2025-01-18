class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charmap = {}
        max_length = 0

        i, j = 0, 0 
        while j < len(s):
            # window is not valid so contract
            if s[j] in charmap and charmap[s[j]] >= i:
                # move left pointer to after the first occurence of repeated character
                i = charmap[s[j]] + 1
            
            # update the window with the current character
            charmap[s[j]] = j
            # process the window
            max_length = max(max_length, j - i + 1)
            # increment the right pointer
            j += 1
        
        return max_length

    '''
    string s -> find the longest substring without repeating characters -> sliding window

    maintain length of longest valid substring + 2 pointers i and j that represent the start and end of the current window 
        - how can we keep track of existance of a character in current window? -> use hashmap or set for O(1) check
        - [slide] expand right pointer while adding corresponding characters to map until we reach a repeated character
        - [process window] compare the length of the current window [i, j] to the length of the longest window so far 
        - [contract the window] we want to contract the window until it only has 1 copy of the repeated character
            - we can move the left pointer until it reaches the repeated character
            - alternatively we can maintain a mapping between characters and their index -> contract in O(1) time
                - we don't need to delete characters from the map -> if map[char] > i then that character is in the current window
            - we need to delete characters from the map when we contract the window
    
    thus total time complexity is O(n) since we visit each character at most twice
    '''