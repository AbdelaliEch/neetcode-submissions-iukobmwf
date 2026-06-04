class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = Counter(nums)
        
        buckets = [[] for i in range(len(nums))]

        for num in count:
            buckets[count[num] - 1].append(num)

        print(buckets)

        i, j = 0, len(buckets) - 1
        while k > 0:
            if buckets[j] and i < len(buckets[j]):
                res.append(buckets[j][i])
                k-=1
                i+=1
            else:
                j-=1
                i = 0

        return res

# complexity: O(n) O(n)