class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val) # O(1)

    def pop(self) -> None:
        self.stack.pop() # O(1)

    def top(self) -> int:
        return self.stack[-1] # O(1)

    def getMin(self) -> int:
        return min(self.stack) #O(n)
