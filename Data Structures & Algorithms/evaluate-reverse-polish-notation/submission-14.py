class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "-":
                stack.append((stack.pop() - stack.pop()) * -1)
            elif token == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(math.trunc(num2 / num1))
            else:
                stack.append(int(token))
        # print(stack)
        return stack[0]
