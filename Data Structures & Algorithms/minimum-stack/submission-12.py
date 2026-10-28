class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        current_min = val if not self.stack or val < self.stack[-1][1] else self.stack[-1][1]
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
#O(1)
