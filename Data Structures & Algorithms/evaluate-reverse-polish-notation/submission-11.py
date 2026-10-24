class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2 - num1)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(math.trunc(num2 / num1))
            else:
                stack.append(int(token))
        return stack[0]

# time: O(n)
# space: O(n)


# ["1","2","+","3","*","4","-"]
# stack = [1 2]