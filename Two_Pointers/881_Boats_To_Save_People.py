from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sort the array -> O(nlogn)
        people.sort()

        nofboats = 0
        i, j = 0, len(people) - 1
        while i <= j:
            # last person needs their own boat
            if i == j:
                nofboats += 1
                break
            # valid pairing can be formed between heaviest and lightest
            elif people[i] + people[j] <= limit:
                nofboats += 1
                i += 1
                j -= 1
            # no valid pairing can be formed between heaviest and lightest
            else:
                nofboats += 1
                j -= 1

        return nofboats

    '''
    people[i] represents the weight of the ith person
    each boat can carry a maximum weight of limit (can have infinite!)
    each boat can carry at most 2 people
    what is the minimum number of boats to carry every person?

    people is an array if integers -> sort?
    we want to pair together the lightest and heaviest people -> pointers to start and end of sorted list
        - people[i] <= weight so there is no person heavier than the boat
    so iterate through the array with the pointers i, j:
        (1) if people[i] + people[j] <= limit then (i)  only need one boat
                                                   (ii) increment i + decrement j
        (2) if people[i] + people[j] > limit then (i)  need a whole boat for jth person (no valid pair)
                                                  (ii) decrement j
        (3) if i == j then we need one boat for the ith person (no valid pair)
    
    thus total time complexity is O(nlogn) and total space complexity is O(1)
    '''
        