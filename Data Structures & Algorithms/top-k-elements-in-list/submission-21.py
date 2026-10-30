class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = [[] for _ in range(len(nums))]
        for num in counter:
            buckets[counter[num] - 1].append(num)

        output = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) >= k:
                    return output

# time: O(n) with n length of nums
# space: O(n) auxiliary space