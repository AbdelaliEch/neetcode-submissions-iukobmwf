class Solution:
    def isValidParentheses(self, lst):
        # to do
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

    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def dfs(depth, current_combination):
            if depth == n * 2:
                if self.isValidParentheses(current_combination):
                    current_combination_string = "".join(current_combination) 
                    output.append(current_combination_string)
                return

            for choice in ("(", ")"):
                current_combination.append(choice)
                dfs(depth + 1, current_combination)
                current_combination.pop()

        dfs(0, [])
        return output


# print(current_combination, choice, current_combination + [choice])
# if not self.isValidParentheses(current_combination + [choice]):
#     continue
