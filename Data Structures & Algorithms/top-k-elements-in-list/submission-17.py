class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums))]
        counter = Counter(nums)

        for num in counter:
            buckets[counter[num] - 1].append(num)

        output = []
        for bucket in buckets[::-1]:
            for num in bucket:
                output.append(num)
                if len(output) == k:
                    return output


# time: O(n) with n length of nums
# space: O(n)

