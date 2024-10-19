from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # process the initial window starting at index 0 and ending at index k - 1
        combined_difference = 0
        for i in range(k):
            # combined_difference = |arr[0] - x| + |arr[1] - x| + ... + |arr[k-1] - x|
            difference = abs(arr[i] - x)
            combined_difference += difference
        # keep track of the window with the smallest combined difference and its value
        smallest, smallest_index = combined_difference, 0

        i, j = 1, k
        while j < len(arr):
            # update the combined difference of the new window
            combined_difference -= abs(arr[i-1] - x)
            combined_difference += abs(arr[j] - x)

            # process the window
            if combined_difference < smallest:
                smallest = combined_difference
                smallest_index = i
            
            # increment left and right pointers to get the next window
            i += 1
            j += 1
        
        return arr[smallest_index:smallest_index + k]
        
    '''
    arr is SORTED, return the k CLOSEST integers to x in the array

    since array is sorted then the k closest integers should form a subarray
    so we want to find the subarray with size k with the combined smallest difference from x -> sliding window!!!

    lets formulate a sliding window solution:
        - keep track of the window with the smallest combined difference and its value
        - initial window starts at index 0 and ends at index k - 1
            - iterate through all elements and calculate combined difference
            - combined_difference = |arr[0] - x| + |arr[1] - x| + ... + |arr[k-1] - x|
        - process the window: check if combined_difference < smallest
        - increment left and right pointers to get the next window
            - combined_difference -= |arr[i] - x|
            - combined_difference += |arr[j] - x|
    since we visit each element exactly twice then the total time complexity is O(n)
    '''
        