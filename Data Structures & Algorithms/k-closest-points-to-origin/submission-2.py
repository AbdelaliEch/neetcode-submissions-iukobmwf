class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for p in points:
            negative_distance = -math.sqrt(p[0]**2 + p[1]**2)
            if len(max_heap) < k:
                heapq.heappush(max_heap, (negative_distance, p))
            elif negative_distance > max_heap[0][0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (negative_distance, p))
        

        print(max_heap)
        output = [coord for _, coord in max_heap]
        print(output)
        return output
        # for _, coord in max_heap:
        #     output



        # for p in points:
        #     heapq.heappush(heap, (math.sqrt(p[0]**2 + p[1]**2), p))

        # output = []
        # for i in range(k):
        #     output.append(heapq.heappop(heap)[1])
        # return output

# time: O(nlogn + klogn) = O(max(n, k)logn) with n lenght of points
# space: O(n) auxiliary space, output space: O(k)