class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        for i, num in enumerate(nums):
            while q and num > q[-1][1]:
                q.pop()
            q.append((i, num))

            if q[0][0] < i - k + 1:
                q.popleft()

            if i >= k - 1:
                output.append(q[0][1])
        return output