class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            heapq.heappush(heap, (math.sqrt(p[0]**2 + p[1]**2), p))

        output = []
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        return output



# we can use a tuple, we will push

# wait why don't we push the euclidean distance instead, but in that case we won't know which point

# so the tuple that we will push is: (euclidean distance, x, y)