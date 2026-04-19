class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                if token == "+":
                    stack.append(val2 + val1)
                elif token == "-":
                    stack.append(val2 - val1)
                elif token == "*":
                    stack.append(val2 * val1)
                elif token == "/":
                    stack.append(int(val2 / val1))
        return stack[0]

# time: O(n)
# space: O(n)

