from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [-1 for _ in range(len(nums))]

        def longestSequence(i):
            # longest subsequence that can be formed with the last num is of length 1
            if i == len(nums) - 1:
                return 1
            # check if subproblem has already been computed
            elif dp[i] != -1:
                return dp[i]

            longest = 1
            # compute longest subsequence with i
            for j in range(i + 1, len(nums)):
                # check all integers greater than nums[i]
                if nums[j] > nums[i]:
                    longest = max(longest , 1 + longestSequence(j))

            # memoize
            dp[i] = longest
            return dp[i]
        
        # compute the longest increasing subsequence starting at every index (we still only compute O(n^2) subproblems total)
        longest_incr_seq = 0
        for i in range(len(nums)):
            longest_incr_seq = max(longest_incr_seq, longestSequence(i))

        return longest_incr_seq

    '''
    nums -> integer array
        - no sorting since order of integers need to be preserved
        - hashing? (maybe), binary search? (no), sliding window? (no since subsequence)
    
    let's examine the brute force solution -> DFS
        - for each index i, check if i is in the longest subsequence or not
            - find the longest subsequence with i 
            - find the longest subsequence without i
            - compare the length of the two subsequences found and return the longest sequence 
    thus the total time complexity of this solution is O(2^n)

    but observe that the brute force solution is recursive with overlapping subproblems -> DP + memoization?
    recall that at each index i, either:
        - nums[i] is in the longest subsequence -> return 1 + dfs(i + 1, nums[i])
        - nums[i] is not in the longest subsequence -> return dfs(i + 1, prev)
    this solution would be 2D DP -> needs to keep track of previous term in the sequence too -> can we do better?

    what if instead of checking the i + 1 index, we check all integers that are greater than nums[i]
    so at each index i, find the longest subsequence starting with i:
        - for each nums[j] > nums[i] with j > i -> return 1 + dfs(j)
        - compare the longest subsequence for each possibility and return the longest one
    we can use memoization to cache the results of smaller subproblems!!!
    thus total time complexity is O(n^2) and total space complexity is O(n) 
    '''