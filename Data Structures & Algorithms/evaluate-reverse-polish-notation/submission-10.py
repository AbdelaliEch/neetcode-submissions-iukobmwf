class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
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
                    stack.append(math.trunc(num2 / num1))
        return stack[0]

# time: O(n)
# space: O(n)


# ["1","2","+","3","*","4","-"]
# stack = [1 2]