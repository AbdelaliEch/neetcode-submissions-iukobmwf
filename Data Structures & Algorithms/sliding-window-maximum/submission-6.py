class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()

        for i in range(k):
            # print(i, nums[i], q)
            while q and nums[i] > q[-1][1]:
                q.pop()
            q.append((i, nums[i]))
        output.append(q[0][1])

        print()
        for i in range(k, len(nums)):
            # print("start", i, nums[i], q, output)
            while q and nums[i] > q[-1][1]:
                q.pop()
            q.append((i, nums[i]))

            # print("mid", i, nums[i], q, output)
            # print(q, q[0][0], i, k, i - k +1)
            if q[0][0] < i - k + 1:
                q.popleft()
            # print("end", i, nums[i], q, output)
            
            output.append(q[0][1])
            # print(output)
            # print()

        return output

# we need to use monotonic decreasing deque


