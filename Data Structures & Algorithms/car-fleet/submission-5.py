import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = list(zip(position, speed))     
        position_speed.sort(key=lambda x: x[0], reverse=True)
        fleets_stack = []
        for pos, sp in position_speed:
            count = (target - pos) / sp
            if not fleets_stack or count > fleets_stack[-1]:
                fleets_stack.append(count)
        return len(fleets_stack)

# time: O(nlogn)
# space: O(n)