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

    def isStillValidParentheses(self, lst, open_count, closed_count, n, choice):
        if open_count == n and choice == "(":
            return False
        if closed_count == n and choice == ")": 
            return False
        
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

        def dfs(depth, current_combination, open_count, closed_count):
            
            if depth == n * 2:
                # if self.isValidParentheses(current_combination):
                current_combination_string = "".join(current_combination) 
                output.append(current_combination_string)
                return

            for choice in ("(", ")"):
                if not self.isStillValidParentheses(current_combination + [choice], open_count, closed_count, n, choice):
                    continue

                current_combination.append(choice)
                if choice == "(":
                    open_count += 1
                else:
                    closed_count += 1
                

                dfs(depth + 1, current_combination, open_count, closed_count)

                current_combination.pop()
                if choice == "(":
                    open_count -= 1
                else:
                    closed_count -= 1
                

        dfs(0, [], 0, 0)
        return output
