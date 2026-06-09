class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for token in tokens:
            print(token, stack)
            if token not in operators:
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                if token == "+":
                    stack.append(b + a)
                if token == "-":
                    stack.append(b - a)
                if token == "*":
                    stack.append(b * a)
                if token == "/":
                    print(a, b)
                    stack.append(int(b / a))
                    # stack.append(a // b)
        return stack.pop()
                

# ["1","2","+","3","*","4","-"]


# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

# (((9 + 3) * -11) / 6) * 10 + 17 + 5

