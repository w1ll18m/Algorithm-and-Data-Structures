class TimeMap(object):

    def __init__(self):
        self.keymap = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """

        if key in self.keymap:
            self.keymap[key].append([timestamp, value])
        else:
            self.keymap[key] = [[timestamp, value]]
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """

        if key not in self.keymap:
            return ""

        timestamp_arr = self.keymap[key]
        start = 0
        end = len(timestamp_arr) - 1
        max_index = -1

        while start <= end:
            middle = (start + end) // 2

            if timestamp_arr[middle][0] > timestamp:
                end = middle - 1
            else:
                if max_index == -1 or timestamp_arr[middle][0] > timestamp_arr[max_index][0]:
                    max_index = middle
                start = middle + 1
        
        if max_index == -1:
            return ""
        else:
            return timestamp_arr[max_index][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

'''
TimeMap must store multiple values for same key at different time stamps 
    - should be indexed by key and time stamp
    - thus use hash map for O(1) retrieval by key

get returns a value with a timestamp less than or equal to the specified timestamp
    - since timestamps of set are strictly increasing then we can store timestamps as a sorted array
    - thus we can efficiently search for a timestamp using binary search
'''