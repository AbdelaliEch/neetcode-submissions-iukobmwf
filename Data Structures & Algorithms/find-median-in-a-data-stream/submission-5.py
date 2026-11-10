class MedianFinder:

    def __init__(self):
        self.smallest_numbers_max_heap = []
        self.largest_numbers_min_heap = []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallest_numbers_max_heap, -1 * num)

        if (self.smallest_numbers_max_heap and self.largest_numbers_min_heap
            and self.smallest_numbers_max_heap[0] * -1 > self.largest_numbers_min_heap[0]):
            val = -1 * heapq.heappop(self.smallest_numbers_max_heap)
            heapq.heappush(self.largest_numbers_min_heap, val)
        
        if len(self.smallest_numbers_max_heap) > len(self.largest_numbers_min_heap) + 1:
            val = -1 * heapq.heappop(self.smallest_numbers_max_heap)
            heapq.heappush(self.largest_numbers_min_heap, val)

        if len(self.largest_numbers_min_heap) > len(self.smallest_numbers_max_heap) + 1:
            val = -1 * heapq.heappop(self.largest_numbers_min_heap)
            heapq.heappush(self.smallest_numbers_max_heap, val)


    def findMedian(self) -> float:        
        if len(self.smallest_numbers_max_heap) > len(self.largest_numbers_min_heap):
            return self.smallest_numbers_max_heap[0] * -1
        if len(self.largest_numbers_min_heap) > len(self.smallest_numbers_max_heap):
            return self.largest_numbers_min_heap[0]
        return (self.smallest_numbers_max_heap[0] * -1 + self.largest_numbers_min_heap[0]) / 2



# we are looking for O(logn) for addition, so we need a heap
# we will use two heaps, one will keep the smallest numbers and one for the largest numbers
# the median will be either the max of smallest numbers, the min of the largest numbers or the sum of the max and min divided by two
# since we need the max of smallest numbers, so it must be a maxheap, and vice versa for the largest numbers


# we will add by default to the small heap, and then we will do any adjustments needed
# the validity conditions of both heaps are: 
# 1) each number in smallest numbers max heap must be less than numbers in largest numbers min heap <=> max of max heap < min of min heap  
# 2) their length must be either == or different by 1