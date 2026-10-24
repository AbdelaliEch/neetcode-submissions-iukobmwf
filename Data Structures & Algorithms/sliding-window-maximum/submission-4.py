class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque() # deque for indexes
        left = 0
        for right in range(len(nums)):
            # make top of the stack q[0] the max value 
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            q.append(right)
            
            # make sure left is in bounds, use indexes in queue
            if left > q[0]:
                q.popleft()

            if (right + 1) >= k:
                output.append(nums[q[0]])
                left += 1
        return output

# time: O(n)
# space: O(n)

# # [1 2 1 0 4 2 6] k = 3
# l = 4  r = 6            window = [4 2 6] 
# q = {6} 
# output = [2 2 4 4 6]
