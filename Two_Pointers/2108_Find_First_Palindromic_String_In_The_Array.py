from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def checkPalindrome(word):
            i, j = 0 , len(word) - 1
            while i < j:
                if word[i] != word[j]:
                    return False
                i, j = i + 1, j - 1
            return True
        
        # check if each element is a palindrome
        for word in words:
            if checkPalindrome(word):
                # return the first element that is a palindrome
                return word
        
        # no element was a palindrome so return empty string
        return ""
    
    '''
    return the first palindromic string in the array -> two pointers
    iterate through the array and check if each element is a palindrome
    thus total time complexity is O(n * m) where n is the size of the array and m is the size of the largest element
    '''
        