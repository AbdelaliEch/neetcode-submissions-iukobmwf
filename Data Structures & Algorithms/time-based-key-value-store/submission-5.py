class TimeMap:

    def __init__(self):
        self.my_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.my_dict[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        print("getting with:", key, timestamp)
        print("my dict:", self.my_dict)

        if self.my_dict.get(key):
            items = sorted([value for value in self.my_dict[key] if value[1] <= timestamp], key=lambda x: x[1], reverse=True)
        else:
            return ""
        print("items:", items)

        return items[0][0] if items else ""
        # dict_items = [(d_key, value) for d_key in self.my_dict for value in self.my_dict[key] if value[1] <= timestamp]
        # dict_items_sorted = sorted(dict_items, key=lambda x: x[1][1])
        # print(dict_items_sorted)
        # print()
        # return dict_items_sorted[-1][1][0] if dict_items_sorted else ""
