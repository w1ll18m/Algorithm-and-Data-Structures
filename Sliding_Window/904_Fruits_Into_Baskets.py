from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        types = defaultdict(int)
        longest = 0

        i, j = 0, 0
        while j < len(fruits):
            # add/update the index of fruit at right pointer to the hashmap
            types[fruits[j]] = j
            
            # check if window is valid
            if len(types) > 2:
                # find the fruit with the smallest index -> O(1) since max 3 items
                to_delete = min(types, key=types.get)
                # move left pointer to after the smallest index
                i = types[to_delete] + 1
                # delete fruit with smallest index from hashmap since it doesn't exist in window anymore
                types.pop(to_delete)
            
            # process the window (compare it to longest so far)
            longest = max(longest, j - i + 1)

            # increment the window
            j += 1
        
        return longest

    '''
    fruits[i] is the type of fruit the ith tree produces
    only have 2 baskets that can only hold a single type of fruit 
    starting from any tree then what is the max # of continuous trees we can pick from -> longest subarray -> sliding window!!!

    lets formulate a sliding window solution:
        - valid window: exists only two type of fruits in the window
            - how to check if valid window? -> check existance using a set or hashmap
            - how to reduce window? -> map fruit to last position
                - want to get rid of all of one type of fruit 
                - compare last positions of type1 and type2 then increment left pointer to the smaller index
        - process the window: check if j - i + 1 > longest
        - increment right pointer
            - add/update fruits[j] in hashmap
    since we visit each element exactly once then time complexity is O(n)
    '''
        