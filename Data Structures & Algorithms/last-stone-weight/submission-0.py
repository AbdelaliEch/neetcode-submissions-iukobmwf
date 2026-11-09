class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negative_stones = [-stone for stone in stones]
        heap = negative_stones
        heapq.heapify(heap)

        print(heap)  

        while len(heap) > 1:
            s1 = -heapq.heappop(heap)
            s2 = -heapq.heappop(heap) 
            print(s1, s2)

            if s2 < s1:
                heapq.heappush(heap, -(s1 - s2))
            print(heap)
        return -heap[0] if heap else 0
