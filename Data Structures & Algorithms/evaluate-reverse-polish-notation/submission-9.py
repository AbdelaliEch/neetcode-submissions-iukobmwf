class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            # print(token, stack)
            if token.isdigit() or (token[0] == "-" and token[1:].isdigit()):
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "+":
                    stack.append(num2 + num1)
                if token == "-":
                    stack.append(num2 - num1)
                if token == "*":
                    stack.append(num2 * num1)
                if token == "/":
                    # print(num2, num1, math.trunc(num2 // num1), round(num2 // num1), num2 / num1, math.trunc(num2/num1))
                    stack.append(math.trunc(num2 / num1))
            # print(token, stack)
            # print()
        return stack[0]

# ["1","2","+","3","*","4","-"]
# stack = [1 2]