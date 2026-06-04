class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict(Counter(nums))
        freq_ordered = sorted(count, key=lambda x: count[x], reverse=True)

        return freq_ordered[:k]