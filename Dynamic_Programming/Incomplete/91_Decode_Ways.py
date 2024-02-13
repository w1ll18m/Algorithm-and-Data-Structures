class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        lofs = len(s)
        N = [None] * lofs
        
        if s[0] != "0":
            N[0] = 1
        else:
            return 0

        N[1] = 2

        for i in range(2, lofs):
            if s[i-1] == 0 or s[i-1] > 2 or (s[i-1] == 2 and s[i] > 6):
                N[i] = N[i-1]
            else:
                N[i] = N[i-1] + N[i-2]
        
        return N[lofs-1]

        # let N[i] be the number of ways to decode the first i digits
        # N[0] = 1 because there is only 1 way to decode a 1 digit message
        #   - exception occurs when the digit is 0
        # N[1] = 2 because there are 2 ways to decode a 2 digit message
        #   - exception occurs as explained below
        # case 1: the ith digit is in a group of 1 digit -> N[i] = N[i-1]
        # case 2: the ith digit is in a group of 2 digits -> N[i] = N[i-2]
        #   - exception occurs when the i-1th digit is zero
        #   - exception occurs when the i-1th digit is greater than 2
        #   - exception occurs when the i-1th digit is 2 but the ith digit is greater than 6
        # therefore it must be that N[i] = N[i-1] + N[i-2] when there is no exception
        # and N[i] = N[i-1] when there is an exception