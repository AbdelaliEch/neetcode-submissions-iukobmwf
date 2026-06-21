class TimeMap:

    def __init__(self):
        self.my_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.my_dict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        print("getting with", key, timestamp)
        if self.my_dict.get(key):
            values = self.my_dict[key]
            print("values", values)
            l, r = 0, len(values) - 1
            current_min = values[0]
            print("initial current min", current_min)
            while l <= r:
                m = (l + r) // 2
                print("left mid right", l, m, r)
                if values[m][1] > timestamp:
                    r = m - 1
                elif values[m][1] < timestamp:
                    if values[m][1] > current_min[1]:
                        current_min = values[m]
                        print("values with current min", values[m], current_min)
                    l = m + 1
                else:
                    print("i am here", values[m])
                    current_min = values[m]
                    break
            if current_min[1] <= timestamp:
                print("last current min", current_min, current_min[0])
            else:
                print("last current min", "empty string")
            print()
            return current_min[0] if current_min[1] <= timestamp else ""
        else:
            return ""

# [('one', 5), ('two', 10), ('three', 15)]

        

# complexity: 
#            for set: O(1) time
#            for get: O(nlogn) time and O(m * n)