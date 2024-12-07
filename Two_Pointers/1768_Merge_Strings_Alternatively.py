class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = ''

        i, j = 0, 0
        while i < len(word1) or j < len(word2):
            if i >= len(word1):
                new += word2[j]
                j += 1

            elif j >= len(word2):
                new += word1[i]
                i += 1
            
            elif i == j:
                new += word1[i]
                i += 1
            
            else:
                new += word2[j]
                j += 1
        
        return new
    
    '''
    merge word1 and word2 based on alternating order -> 2 pointers
    thus total time complexity is O(n + m) where n and m are the length of word1 and word2 respectively
    '''