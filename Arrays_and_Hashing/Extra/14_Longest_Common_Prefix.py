from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        common_prefix = ""
        
        shortest = strs[0]
        longest = strs[-1]

        for i in range(len(shortest)):
            if shortest[i] == longest[i]:
                common_prefix = common_prefix + shortest[i]
            else:
                break
        
        return common_prefix

    '''
    sort the array 
    compare the first and last strings which are shortest and longest strings respectively
    '''