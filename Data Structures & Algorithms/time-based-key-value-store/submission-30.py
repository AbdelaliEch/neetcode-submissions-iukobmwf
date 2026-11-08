class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        d = self.data[key]

        current_max_idx = -1
        left, right = 0, len(d) - 1
        while left <= right:
            mid = (left + right) // 2
            if d[mid][0] > timestamp:
                right = mid - 1
            else:
                current_max_idx = mid 
                left = mid + 1
        return d[current_max_idx][1] if current_max_idx != -1 else ""



# [(1, 'happy'), (2, 'sad'), (3, 'angry')]