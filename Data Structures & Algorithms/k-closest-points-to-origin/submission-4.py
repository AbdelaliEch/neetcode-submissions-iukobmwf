class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for p in points:
            negative_distance = -(p[0]**2 + p[1]**2)
            if len(max_heap) < k:
                heapq.heappush(max_heap, (negative_distance, p))
            elif negative_distance > max_heap[0][0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (negative_distance, p))

        output = [coord for _, coord in max_heap]
        return output
     

# time: O(nlogk) with n length of points
# space: O(k)