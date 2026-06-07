class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums))]
        counter = Counter(nums)
        res = []

        for num in counter:
            buckets[counter[num] - 1].append(num)

        i = len(buckets) - 1

        while k > 0:
            if buckets[i]:
                j = 0
                while j < len(buckets[i]):
                    res.append(buckets[i][j])
                    j+=1
                    k -= 1
            i -= 1

        return res
