class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        stack = []

        for p, s in position_speed:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)

# time: O(nlogn) with n size of inputs lists
# space: O(n)