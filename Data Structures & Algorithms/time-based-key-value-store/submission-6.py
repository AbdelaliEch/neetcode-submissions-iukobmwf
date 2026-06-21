class TimeMap:

    def __init__(self):
        self.my_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.my_dict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if self.my_dict.get(key):
            items = sorted([value for value in self.my_dict[key] if value[1] <= timestamp], key=lambda x: x[1], reverse=True)
        else:
            return ""

        return items[0][0] if items else ""
        

# complexity: 
#            for set: O(1) time
#            for get: O(nlogn) time and O(m * n)