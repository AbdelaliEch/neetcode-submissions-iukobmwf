class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)  

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        d = self.data[key]
        left, right = 0, len(d) - 1
        current_max = -1
        while left <= right:
            mid = (left + right) // 2
            if d[mid][1] > timestamp:
                right = mid - 1
            else:
                # print("new max")
                current_max = mid
                left = mid + 1
        return d[current_max][0] if current_max != -1 else ""

