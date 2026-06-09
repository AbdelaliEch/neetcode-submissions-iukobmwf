class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            minVal = val
        else:
            minVal = min(val, self.stack[-1][1])
    
        self.stack.append((val, minVal))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# [(1, 1), ()]



# to get the min of the stack, maybe we should keep tracking it from the initialization of the stack
# each time we push to the stack, we track if it is a new min
# but we need to handle also popping from it?????

# so what if we store instead of normal values, we store the current min with each value
# so that when we pop one, we can always check the top and see what was the last min


