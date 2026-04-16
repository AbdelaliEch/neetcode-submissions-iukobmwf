class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freq_dict = Counter(nums)
        most_common = freq_dict.most_common(k)
        print(most_common)
        for i in range(k):
            result.append(most_common[i][0])
        return result

# Time: O(n * log n)
# Space: O(n)