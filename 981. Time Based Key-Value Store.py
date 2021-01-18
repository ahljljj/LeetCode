# 981. Time Based Key-Value Store


#2021/01/17, binary search + hash table

# time: set O(1), get O(log N)

# Runtime: 788 ms, faster than 35.93% of Python3 online submissions for Time Based Key-Value Store.
# Memory Usage: 71.4 MB, less than 8.32% of Python3 online submissions for Time Based Key-Value Store.

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key] = [[value, timestamp]]
        else:
            self.m[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        return self.search(self.m[key], timestamp)

    def search(self, values, target):
        l, r = 0, len(values) - 1
        while l + 1 < r:
            m = (l + r) >> 1
            if values[m][1] < target:
                l = m
            else:
                r = m
        if values[r][1] <= target:
            return values[r][0]

        if values[l][1] <= target:
            return values[l][0]

        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)