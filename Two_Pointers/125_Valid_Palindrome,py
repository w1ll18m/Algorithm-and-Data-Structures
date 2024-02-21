class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.lower()                                                       # convert to lowercase
        left = 0                                                            # keeps track of index of forward character
        right = len(s) - 1                                                  # keeps track of index of backwards character

        while(left < right):                                                # if left >= right then the string must be a palindrome
            while not (s[left].isalpha() or s[left].isnumeric()):           # skip non-alphanumeric characters
                if left == right:
                    break
                left += 1
            while not (s[right].isalpha() or s[right].isnumeric()):         # skip non-alphanumeric characters
                if left == right:
                    break
                right -= 1
            
            if s[left] != s[right]:                                         # check if next forward character is the same as the next backwards character
                return False
            left += 1
            right -= 1
        
        return True
        