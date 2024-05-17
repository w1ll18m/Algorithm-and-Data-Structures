class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                solutions.append(subset.copy())
                return
            
            # decision to include i in the subset
            subset.append(nums[i])
            dfs(i + 1)

            # decision not to include i in the subset
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        
        return solutions

    '''
    observe that for each item in the number it is either:
        - in the subset
        - not in the subset
    thus we can recursively build all of the subsets
    '''
        