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
    
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]  



# now the heap contains the top k largest, and the k largest is root


# to keep k largest, we need to use min heap

# [1 2 3 3]
# [-1 -2 -3 -3]
# heap = [-3 -1 -2]
# so first element is the largest and last element is not necessarily the kth largest because it isn't sorted

# what if we did smallest, k largest is n - k smallest, 2 largest is

# root will always represent either the most largest ot most smallest
# my issue is: when adding another value i should compare it with what



# [1 2 3 3 4 5] 3
# heap will tell us which one is the smallest or largest
# heap with size k will tell us which is the k smallest or k largest

# now we have top k largest, the index 0 is the largets

# when size will be bigger than k, 

# []