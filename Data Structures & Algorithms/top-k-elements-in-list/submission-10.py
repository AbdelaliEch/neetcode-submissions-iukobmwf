class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        count_sorted = sorted(Counter(nums).items(), key= lambda x: x[1], reverse=True)

        for pair in count_sorted[:k]:
            output.append(pair[0])

        return output