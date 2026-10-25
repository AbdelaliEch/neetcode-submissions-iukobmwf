class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed_position = zip(position, speed)
        speed_position_sorted = sorted(speed_position, key= lambda x: x[0], reverse=True)
        stack = []
        for sp in speed_position_sorted:
            time = (target - sp[0]) / sp[1]
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)

# time: O(nlogn)
# speed: O(n)

# time needed to reach target is: t = (target - position) / speed
# [7 4 1 0] [1 2 1 1]

# the stack needs to be decreasing, so 

#if a car catches up??? that means we need to handle cars that are in advance first right?