class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)       

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

# time: O(1)

    def get(self, key: str, timestamp: int) -> str:
        dt = self.data[key]
        # print("get", key, timestamp, dt)

        current_max = None
        left, right = 0, len(dt) - 1
        while left <= right:
            middle = (left + right) // 2
            # print(left, middle, right)
            mid_timestamp = dt[middle][1] 
            if mid_timestamp > timestamp:
                right = middle - 1
            # less or equal, the range we want, but we want its max, which is to the right, or it can be the max itself
            # so we better store it
            else:
                current_max = middle
                left = middle + 1
        # so now we have current max, but what if it wasn't set, it will stay none then
        # print("current max", current_max)
        return dt[current_max][0] if current_max != None else "" 


# we are looking for the largest prev timestamp that is <= timestamp
# we are appending in an ascending way