class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # print("called push", self.stack)
        if not self.stack or val < self.stack[-1][1]:
            current_min = val
        else:
            current_min = self.stack[-1][1]
        
        self.stack.append((val, current_min))
        # print("after called push", self.stack)


    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# we need to push an element with current min when it was pushed
