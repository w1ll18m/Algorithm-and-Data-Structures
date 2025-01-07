from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # initialize the array for memoization
        dp = [None for _ in range(len(s))]

        # convert the list of words to a set
        wordMap = set()
        for word in wordDict:
            wordMap.add(word)

        def checkValidSequence(i):
            # if substring is empty the return True
            if i >= len(s):
                return True
            # check if subproblem has already been computed
            elif dp[i] is not None:
                return dp[i]
            
            cur_substring = ""
            # iterate over substring to check all prefixes
            for j in range(i, len(s)):
                cur_substring += s[j]
                # check if prefix results in valid segmentation
                if cur_substring in wordMap and checkValidSequence(j + 1):
                    # memoize
                    dp[i] = True
                    return dp[i]
            
            # memoize
            dp[i] = False
            return dp[i]
        
        return checkValidSequence(0)
            
    '''
    wordDict -> list of strings
    return true if s can be segmented into a space-separated sequence of 1+ words

    we want to be able to check if a string is in wordDict in O(1) time -> convert list to dict
    need to keep track of the current string
        - if the current substring is empty then return True
        - for each prefix that matches a string in wordDict:
            - recurse on rest of the substring (without the prefix) -> CAN BE MEMOIZED
        - if any of the prefix result in a valid segmentation then return True (use OR)
    we can memoize the results for smaller substrings to quickly check if they are valid

    thus total time complexity is O(n^2) 
    '''