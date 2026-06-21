class TimeMap:

    def __init__(self):
        self.my_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.my_dict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if self.my_dict.get(key):
            values = self.my_dict[key]
            l, r = 0, len(values) - 1
            current_min = values[0]
            while l <= r:
                m = (l + r) // 2
                if values[m][1] > timestamp:
                    r = m - 1
                elif values[m][1] < timestamp:
                    if values[m][1] > current_min[1]:
                        current_min = values[m]
                    l = m + 1
                else:
                    current_min = values[m]
                    break
            return current_min[0] if current_min[1] <= timestamp else ""
        else:
            return ""

# [('one', 5), ('two', 10), ('three', 15)]

        

# complexity: 
#            for set: O(1) time
#            for get: O(logn) time and O(m * n)