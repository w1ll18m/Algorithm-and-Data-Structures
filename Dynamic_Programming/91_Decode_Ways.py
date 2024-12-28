class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1 for _ in range(len(s))]

        def findDecodings(i):
            # if string has been decoded successfully then return 1
            if i >= len(s):
                return 1
            # if string starts with 0 then it can not be decoded
            elif int(s[i]) == 0:
                return 0
            # check if subproblem has been computed already
            elif dp[i] != -1:
                return dp[i]
            
            # find # of possibilities if decode i by itself
            direct = findDecodings(i + 1)
            # if s[i] can only be decoded by itself then set together = 0
            if i == len(s) - 1 or int(s[i]) > 2 or (int(s[i]) == 2 and int(s[i+1]) > 6):
                together = 0
            # find # of possibilities if decode i and i+1 together
            else:
                together = findDecodings(i + 2)
            
            # add total # of ways from both possibilities + memoize
            dp[i] = direct + together
            return dp[i]

        return findDecodings(0)

    '''
    given a string s containing only digits, return the # of ways to decode it
        - no sorting since digits must remain in order
    hashing? (no), binary search? (no), sliding window? (no cuz we would need to consider all windows)

    observe that for any given number i, either:
        - if s[i] == 0 then the message can not be decoded
        - if i >= len(s) then the message has been decoded successfully so return 1
        - if 1 <= s[i] <= 2 then (i) s[i] can be decoded as follows:
            - s[i] is decoded directly -> 1 * numDecodings[i+1]
            - s[i] and s[i+1] are decoded together -> 1 * numDecodings[i+2]
                - if s[i] == 2 and s[i+1] > 6 then they can not be decoded together
                - if s[i] > 2 then they can not be decoded together
                - if i == len(s) - 1 then they can not be decoded together
            - so total # of ways is numDecodings[i+1] + numDecodings[i+2]
            - if numDecodings[i+1] and numDecodings[i+2] are both 0 then there are no ways to decode the string
    
    we can optimize this solution with memoization (top-down dp)
    since we visit each index at most once then the total time complexity is O(n)
    '''