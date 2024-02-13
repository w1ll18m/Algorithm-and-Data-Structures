class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        lofs = len(s)
        P = [None] * lofs
        P[0] = 1

        for i in range(1, lofs):
            for j in range(i + 1):
                ipos = i
                jpos = j
                curlen = 0

                while s[jpos] == s[ipos] and jpos < ipos:
                    curlen += 2
                    ipos -= 1
                    jpos += 1
                if jpos == ipos:
                    curlen += 1

                if jpos >= ipos:
                    P[i] = curlen
                    break
            
            P[i] = max(P[i], P[i-1])
        
        index = lofs - 1
        while index > 0 and P[index] == P[index-1]:
            index -= 1
        
        palin_end = index + 1
        palin_start = index - P[index] + 1
        return s[palin_start:palin_end]


        # let P[i] represent the longest palindromic substring with the first i characters
        # P[0] = 1
        # P[i] = P[i-1] -> ith character is not in the longest substring
        # OR
        # P[i] = (iterate through string from beginning and compare to palindrome ending with ith character)