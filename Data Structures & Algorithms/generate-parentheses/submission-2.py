class Solution:
    def isValidParentheses(self, lst):
        stack = []
        for c in lst:
            if c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack

    def isStillValidParentheses(self, lst):
        stack = []
        for c in lst:
            if c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True

    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def dfs(depth, current_combination, open_parentheses_count, closed_parentheses_count):
            
            if depth == n * 2:
                if self.isValidParentheses(current_combination):
                    current_combination_string = "".join(current_combination) 
                    output.append(current_combination_string)
                return

            for choice in ("(", ")"):
                if open_parentheses_count == n and choice == "(":
                    continue
                if closed_parentheses_count == n and choice == ")": 
                    continue
                
                if not self.isStillValidParentheses(current_combination + [choice]):
                    continue

                current_combination.append(choice)
                if choice == "(":
                    open_parentheses_count += 1
                else:
                    closed_parentheses_count += 1
                

                dfs(depth + 1, current_combination, open_parentheses_count, closed_parentheses_count)

                current_combination.pop()
                if choice == "(":
                    open_parentheses_count -= 1
                else:
                    closed_parentheses_count -= 1
                

        dfs(0, [], 0, 0)
        return output
