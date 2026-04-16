class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        freq_dict_sort = sorted(freq_dict.keys(), key=lambda x: freq_dict[x], reverse=True)
        print(freq_dict)
        print(freq_dict_sort)
        return freq_dict_sort[:k]