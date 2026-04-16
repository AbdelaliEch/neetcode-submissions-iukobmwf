class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        bucket = [[] for i in range(len(nums))]
        result = []
        print(f"frequency: {frequency}")
        print(f"bucket: {bucket}")
        for num in frequency:
            bucket[frequency[num] - 1].append(num)
        i, j = len(nums) - 1, 0
        # print(bucket[i])
        while k > 0:
            print(bucket[i])
            if bucket[i] and j < len(bucket[i]):
                result.append(bucket[i][j])
                k -= 1
                j += 1
            else:
                i -= 1
                j = 0
        return result


# Time: O(n) +
# Space: O(n) + 