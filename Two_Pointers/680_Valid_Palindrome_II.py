class Solution:
    def validPalindrome(self, s: str) -> bool:
        # initialize two pointers to check values at start and end of string
        i, j = 0, len(s) - 1

        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True

        while i < j:
            # check if values at pointers are not equal
            if s[i] != s[j]:
                # check if deleting value at pointer 1 or deleting value at pointer 2 results in valid palindrome
                return isPalindrome(i + 1, j) or isPalindrome(i, j - 1)
            i, j = i + 1, j - 1
        return True
        
    '''
    return true if a string can be a palindrome after deleting at most one character -> 2 pointers
    (1) maintain 2 pointers at the start and end of the string
    (2) if i < j:
             (i) if the values at the pointers are equal then move both pointers
            (ii) if the values at the pointers are not equal (no character has been deleted)
                - delete value at pointer 1 -> increment pointer 1 -> continue checking
                - delete value at pointer 2 -> increment pointer 2 -> continue checking
    instead of deleting the value, we can just maintain the indexes of the values that caused the initial error
    thus we check each character at most twice so total time complexity is O(n) and total space complexity is O(1)
    '''