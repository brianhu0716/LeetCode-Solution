# algorithm
"""
when the "set" been called, we need to save the value and timestamp for given key, and the order of value list need to be sorted according to timestamp so that when
"get" been called we can use binary search to find the nearest timestamp to given timestamp and return the corresponding value
"""

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key]["timestamp"] = [timestamp]
            self.d[key]["value"] = [value]
            return
        i, j = 0, len(self.d[key]["timestamp"]) - 1
        lst = self.d[key]["timestamp"]
        while i <= j: # use binary search to find the position where we need to insert timestamp and value to
            mid = (i + j) // 2
            if lst[mid] > timestamp:
                j = mid - 1
            else:
                i = mid + 1
        self.d[key]["timestamp"].insert(i, timestamp)
        self.d[key]["value"].insert(i, value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d or timestamp < self.d[key]["timestamp"][0]: # if key not in d or the timestamp is earlier to the first timestamp in given key, return ""
            return ""
        i, j = 0, len(self.d[key]["timestamp"]) - 1
        lst = self.d[key]["timestamp"]
        while i <= j: # use binary search to find the return value
            mid = (i + j) // 2
            if lst[mid] > timestamp:
                j = mid - 1
            else:
                i = mid + 1
        return self.d[key]["value"][j]