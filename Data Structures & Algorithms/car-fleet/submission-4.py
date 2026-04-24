import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = list(zip(position, speed))     
        position_speed.sort(key=lambda x: x[0], reverse=True)
        print(position_speed)
        fleets_stack = []
        for pos, sp in position_speed:
            count = (target - pos) / sp
            print(pos, count)
            if not fleets_stack or count > fleets_stack[-1]:
                fleets_stack.append(count)
        print(fleets_stack)
        return len(fleets_stack)
