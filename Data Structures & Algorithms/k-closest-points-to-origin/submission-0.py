class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            heapq.heappush(heap, (math.sqrt(p[0]**2 + p[1]**2), p))
        print(heap)

        output = []
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
            # output.append(heap[0][1])
        return output

# we gonna use a heap of size k
# we will push from points array to the heap, the issue is how will we heappush 
# the heap is a min heap

# should i push one value, and then when i will push the next value i will just check if it's smaller than the current value
# if it is, then it is the new min


# or should i 


# we can use a tuple, we will push

# wait why don't we push the euclidean distance instead, but in that case we won't know which point

# so the tuple that we will push is: (euclidean distance, x, y)