class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        nofvowels = 0

        if k > len(s):
            return 0
        for i in range(k):
            if s[i] in vowels:
                nofvowels += 1
        max_vowels = nofvowels

        i, j = 1, k
        while j < len(s):
            if s[i-1] in vowels:
                nofvowels -= 1
            if s[j] in vowels:
                nofvowels += 1
            if nofvowels > max_vowels:
                max_vowels = nofvowels
            i += 1
            j += 1
        
        return max_vowels

'''
find the maximum number of vowels letters in any substring of s with length k
observe that substring of length k implies a fixed sliding window problem
1. maintain 2 pointers i and j where j - i + 1 = k
2. for every iteration:
    a. check if # of vowels is greater than current max
    b. increment i and j by 1
    c. check if s[i-1] and s[j] are vowels then update current nofvowels accordingly
'''