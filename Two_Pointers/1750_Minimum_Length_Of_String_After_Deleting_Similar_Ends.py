class Solution:
    def minimumLength(self, s: str) -> int:
        i, j = 0, len(s) - 1

        # check if we can perform the operation
        while i < j:
            length = j - i + 1
            del_char = s[i]

            # if prefix character and suffix character are not equal then no operation is possible
            if s[i] != s[j]:
                return length
            
            # perform the operation (by moving left and right pointers)
            while i < len(s) and s[i] == del_char:
                i += 1
            while j >= 0 and s[j] == del_char:
                j -= 1
        
        return max(0, j - i + 1)

    '''
    string s -> sliding window? 2 pointers?
    observe that for each string there is only one possible move:
        - if s[0] != s[-1] then no operation can be performed so return len(s)
        - if s[0] == s[-1] then perform the operation

    thus total time complexity is O(n) since we visit each character at most once
    '''