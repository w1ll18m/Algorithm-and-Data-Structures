class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        if len(s) <= 10:
            return []

        sequences = {}
        repeated = []

        for i in range(len(s) - 9):
            subsequence = s[i:i+10]
            if subsequence in sequences:
                if sequences[subsequence] == 1:
                    repeated.append(subsequence)
                    sequences[subsequence] += 1
            else:
                sequences[subsequence] = 1
        
        return repeated
        


        