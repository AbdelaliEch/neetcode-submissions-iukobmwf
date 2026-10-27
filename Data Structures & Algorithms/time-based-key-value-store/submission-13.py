class TimeMap:

    def __init__(self):
        self.data = defaultdict(deque)       

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].appendleft((value, timestamp))

        # self.data[key].sort(key= lambda x: x[1], reverse=True)
        # print(self.data)

    def get(self, key: str, timestamp: int) -> str:
        for value, prev_timestamp in self.data[key]:
            if prev_timestamp <= timestamp:
                return value
        return ""


# time: O()
# space: O()

# i should set in an ordered way
# is there a data