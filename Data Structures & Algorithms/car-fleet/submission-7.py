class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = [(position[i], speed[i]) for i in range(len(position))]
        position_speed.sort(key=lambda x: x[0], reverse=True)
        
        stack = []
        for pos, speed in position_speed:
            steps = (target - pos) / speed
            if not stack:
                stack.append(steps)
            else:
                if steps > stack[-1]:
                    stack.append(steps)
        return len(stack)

# v = d/t
# t = (10 - position) / speed
# [(7, 1), (4, 2), (1, 2), (0, 1)]


# number of iterations each car will take to reach target is:
# x = (target - position) / speed


# target = 10, position = [4,1,0,7], speed = [2,2,1,1]
