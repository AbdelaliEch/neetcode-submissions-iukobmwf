class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for n in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, n)
            elif n > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, n)
        return min_heap[0]