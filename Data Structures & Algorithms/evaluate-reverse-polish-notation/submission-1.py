class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
            else:
                print(stack)
                val1 = stack.pop()
                val2 = stack.pop()
                print(stack, val1, val2)
                if token == "+":
                    stack.append(val2 + val1)
                elif token == "-":
                    stack.append(val2 - val1)
                elif token == "*":
                    stack.append(val2 * val1)
                elif token == "/":
                    stack.append(int(val2 / val1))
                print(stack)
                print()
        return stack[0]

tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
