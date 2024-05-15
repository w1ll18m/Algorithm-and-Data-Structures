class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0

        longest_substring = 1
        seen_chars = dict()

        left = 0
        right = left + 1
        seen_chars[s[left]] = left                                                          # keep track of seen character's position

        while right < len(s):
            if s[right] in seen_chars and seen_chars[s[right]] >= left:                     # case where current character has been seen in the current window/substring
                current_substring = right - left
                longest_substring = max(longest_substring, current_substring)

                left = seen_chars[s[right]] + 1                                             # move left pointer to the position after the repeated character
                seen_chars[s[right]] = right                                                # update the new position of the repeated character
            
            elif right == len(s) - 1:                                                       # edge case where longest substring includes the last character
                current_substring = right - left + 1
                longest_substring = max(longest_substring, current_substring)

                left = right
            
            else:                                                                           # case where current character has not been seen in the current window/substring yet
                seen_chars[s[right]] = right                                                # update the new position of thee repeated character
            
            right += 1
        
        return longest_substring

        '''
        pattern: find the longest (max) subarray that has no repeating characters -> sliding window

        condition to stop expanding the window: see a repeated character
        while expanding: keep track of seen characters and their position (can use hashing for O(1) check)
            - need to keep track of their position because of case such as "dvdf" where vdf is longest
        processing the window: count the number of characters in the subarray
            - also need to move left pointer to position of repeated character + 1
        '''
        