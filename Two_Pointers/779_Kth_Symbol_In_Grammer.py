class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # base: n = 1 -> first layer (only digit is 0)
        if n == 1:
            return 0
        
        nofdigits = 2 ** (n - 1)

        # case: k <= nofdigits / 2 then search previous row
        if k <= nofdigits / 2:
            return self.kthGrammar(n - 1, k)
        # case: k > nofdigits / 2 then search previous row but flip answer
        else:
            return 1 - self.kthGrammar(n - 1, k - (nofdigits / 2))
    
    '''
    table of n rows (1-indexed)
        - write 0 in the 1st row
        - replace each occurrence of 0 in the last row with 01
        - replace each occurrence of 10 with 0

    0
    0 1
    01 10
    0110 1001
    01101001 10010110

    observe that the length of ith row is 2^(i-1) (assuming 1-indexed)
        - the first half of each row is just the previous row
        - the second half of each row is just the complement of the first half
    
    we want to find the kth symbol in the nth row (assuming 1-indexed)
        - length of the nth row is 2^(n-1)
        - if k <= nofdigits / 2 then we need to search the first half -> find the kth symbol in the n-1st row
        - if k > nofdigits / 2 then we need to search the second half -> find the (k - nofdigits / 2)th symbol in the n-1st row (but reverse the bit at the end)

    this looks like a recursive solution!!! -> k = 1 then return 0

    thus the total time complexity is O(logn) since we recurse on half of the array at a time
    '''