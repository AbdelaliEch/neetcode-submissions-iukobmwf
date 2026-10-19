class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        counter = Counter(nums)
        count_sorted = sorted(counter.items(), key= lambda x: x[1], reverse=True)

        for pair in count_sorted[:k]:
            output.append(pair[0])

        return output

# time: O(n + mlog(m)) with n length of nums and m number of distinct numbers
# space: O(n)