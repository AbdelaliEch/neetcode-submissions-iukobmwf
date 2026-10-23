class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        buckets = [[] for _ in range(len(nums))]
        
        counter = Counter(nums)
        for num in counter:
            buckets[counter[num] - 1].append(num)
        # print(buckets) 

        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                if len(output) >= k:
                    return output
                output.append(num)
        return output
            