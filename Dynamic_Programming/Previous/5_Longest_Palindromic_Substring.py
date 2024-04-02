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
            for j in range(i + 1):  # iterate through string from beginning and compare to palindrome ending with ith character
                ipos = i
                jpos = j
                curlen = 0

                while s[jpos] == s[ipos] and jpos < ipos:  
                    curlen += 2
                    ipos -= 1
                    jpos += 1
                if jpos == ipos:
                    curlen += 1

                if jpos >= ipos:    # if jpos >= ipos then s[j:i] is a palindrome otherwise keep checking
                    P[i] = curlen
                    break
            
            P[i] = max(P[i], P[i-1])
        
        index = lofs - 1
        while index > 0 and P[index] == P[index-1]:
            index -= 1
        
        palin_end = index + 1
        palin_start = index - P[index] + 1
        return s[palin_start:palin_end]

        # INEFFICIENT SOLUTION -> wost case time complexity is not polynomial
        #                      -> consider solution that starts from center and iterates outwards
        #                      -> consider the case where we know "BAB" is a palindrome then "CBABC" must be a palindrome too
    
        # ACTUALLY MAYBE IT IS OK BUT WE NEED TO KEEP TRACK OF PREVIOUS PALINDROME -> IF _BAB IS PALINDROME THEN _BABC IS PALINDROME TOO IF _ IS C

        # let P[i] represent the longest palindromic substring with the first i characters
        # P[0] = 1
        # P[i] = P[i-1] -> ith character is not in the longest substring
        # OR
        # P[i] = (iterate through string from beginning and compare to palindrome ending with ith character)
    
        # DECODE WAYS -> let N[i] be the number of ways to decode the first i digits the