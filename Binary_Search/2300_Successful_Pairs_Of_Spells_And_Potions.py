from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # sort potions in non-decreasing order
        potions.sort()
        pairs = [0 for _ in range(len(spells))]

        for k in range(len(spells)):
            # compute the minimum strength that a potion needs to have to form a successful pair
            target = math.ceil(success / spells[k])

            i, j = 0, len(potions) - 1
            first_occurrence = -1
            while i <= j:
                middle = (i + j) // 2
                # if an instance of x has been found
                if potions[middle] == target:
                    # record the index of the matching element
                    first_occurrence = middle
                    # search the left subarray for earlier occurrences
                    j = middle - 1
                # if middle element is less than target then search the right subarray
                elif potions[middle] < target:
                    i = middle + 1
                # if middle element is greater than target then search the left subarray
                else:
                    j = middle - 1

            # if element was found then all elements to the right of the element are valid 
            if first_occurrence != -1:
                pairs[k] = (len(potions) - 1) - first_occurrence + 1
            # if element was not found then all elements to the right of where it would be are valid
            elif i < len(potions):
                pairs[k] = (len(potions) - 1) - i + 1

        return pairs
    
    '''
    spells[i] represents the strength of the ith spell
    potions[i] represents the strength of the jth potion
    a spell and potion pair is considered successful if product is at least success
    
    find pairs where pairs[i] is the # of potions that will form a successful pair with the ith spell
    brute force solution -> for each spell, iterate through all potions and check their product -> O(n * m) time complexity

    observe that for each spell i, the potion must be at least x = math.ceil(success / spell[i])) to form a successful pair
    how do we efficiently find all potions that are greater/equal to x? -> sort O(m log m) + binary search O(log n) 
    for each middle element ((i + j) // 2):
        - if middle element is x then find the first instance of x
        - if middle element is not x then recurse on subarray depending on if middle > x or middle < x
        - if we don't find x then elements to the right of current pointer are valid
    
    thus total time complexity is O(m log m + n log m) = O((m + n) log m)
    '''