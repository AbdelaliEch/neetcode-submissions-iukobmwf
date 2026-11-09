class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for num in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, num)
            elif num > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, num)
    
# time: O(nlogk) with n length of nums and k the input int given
# space: O(k) for the heap space

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]  


# time: O(logk)
# space: O(1)

