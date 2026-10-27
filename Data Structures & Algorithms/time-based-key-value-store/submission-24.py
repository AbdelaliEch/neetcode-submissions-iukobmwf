class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)       

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

# time: O(1)

    def get(self, key: str, timestamp: int) -> str:
        dt = self.data[key]

        current_max = None
        left, right = 0, len(dt) - 1
        while left <= right:
            middle = (left + right) // 2
            mid_timestamp = dt[middle][1] 
            if mid_timestamp > timestamp:
                right = middle - 1
            else:
                current_max = middle
                left = middle + 1
        return dt[current_max][0] if current_max is not None else "" 

# time: O(logn) with n number of values associated with a key



# space: O(m * n) with m number of keys

