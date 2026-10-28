class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = sorted(zip(position, speed), key= lambda x: x[0], reverse=True)
        stack = []
        for ps in position_speed:
            time = (target - ps[0]) / ps[1]
            # print(time)
            if not stack or time > stack[-1]:
                stack.append(time)
        # print(position_speed, stack)
        return len(stack)

