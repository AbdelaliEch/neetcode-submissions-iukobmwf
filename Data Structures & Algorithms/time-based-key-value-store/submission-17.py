class TimeMap:

    def __init__(self):
        self.data = defaultdict(deque)       

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].appendleft((value, timestamp))

# time: O(1)

    def get(self, key: str, timestamp: int) -> str:
        # print(self.data[key])
        if not self.data[key]:
            return ""
        left, right = 0, len(self.data[key]) - 1
        # current_max = self.data[key][0]
        while left < right:
            middle = (left + right) // 2
            prev_timestamp = self.data[key][middle][1]
            if prev_timestamp > timestamp:
                left = middle + 1
            else:
                right = middle
        return self.data[key][left][0] if self.data[key][left][1] <= timestamp else "" 



# time: O(n) with n max number of values associated with a key


# space: O(m * n) with m number of keys and n max number of values associated with a key