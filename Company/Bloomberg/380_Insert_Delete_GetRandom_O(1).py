import random

class RandomizedSet:

    def __init__(self):
        self.nofitems = 0
        self.elementSet = {}
        self.elementArr = []

    def insert(self, val: int) -> bool:
        # if val is in the set then return False
        if val in self.elementSet:
            return False
        
        # add the val to the array of elements
        self.elementArr.append(val)

        # map the val to the index in the array of elements
        self.elementSet[val] = self.nofitems
        
        # increment the # of items in the array
        self.nofitems += 1

        return True

    def remove(self, val: int) -> bool:
        # if val is not in the set then return False
        if val not in self.elementSet:
            return False
        
        # find the index of the val to be removed from the map
        rindex = self.elementSet[val]

        # move val at the end of the array of elements to the "removed" index and update map
        last_val = self.elementArr[-1]
        self.elementArr[rindex] = last_val
        self.elementSet[last_val] = rindex
        del self.elementSet[val]

        # pop the array and update count
        self.elementArr.pop()
        self.nofitems -= 1

        return True

    def getRandom(self) -> int:
        # generate a random number between 0 and len(arr) - 1 and return the value at that index
        randindex = random.randint(0, self.nofitems - 1)
        return self.elementArr[randindex]

'''
insert(int val) -> inserts a val into the set if not present -> hashmap?
remove(int val) -> remove a val from the set if present -> hashmap?
getRandom() -> returns a random element from the current set 

vals can be negative!!! 
can we use random.randint(a, b) to generate a random element in the set? -> no since vals are not contiguous
what if we mapped vals in the set to contiguous values?
    - used an array to hold vals in the set (ex. first val is in index 0, second val is in index 1)
    - generate a random number between 0 and len(arr) - 1 then return the value at that index -> O(1)
    - inserting a new value to this array is easy -> append to end of the array -> O(1)
    - deleting a value from this array is hard -> remove a certain index from the array -> O(n)
        - potential sol: don't remove index, add it to a stack of "available" indices instead
            - calling random.randint can potentially generate one of these removed indices -> not equal prob for set elements!!!
        - potential sol: move element in last index to "removed" index then pop the last element -> O(1)

thus total time complexity is O(1) and total space complexity is O(n)
'''


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()