class Solution:
    def climbStairs(self, n: int) -> int:
        # intialize the memoization array
        memoize = [-1 for _ in range(n + 1)]
        # there is only one way to reach the top from the last and second last step
        memoize[n] = 1
        memoize[n - 1] = 1

        def findDistinct(i):
            # check if step has not been processed yet
            if memoize[i] == -1:
                # recursively calculate the # of distinct ways
                nofways = findDistinct(i + 1) + findDistinct(i + 2)
                # memoize the result
                memoize[i] = nofways
            return memoize[i]

        return findDistinct(0)
        
    '''
    you can either climb 1 or 2 steps to the top
    observe that at step i:
        - we can either take 1 step or 2 steps
        - then the # of ways you can climb to the top is nofdistinct(i+1) + nofdistinct(i+2)
    thus we can use memoization to solve this recursive problem in O(n) time
    '''