class Solution:
    # def isStillValidParentheses(self, lst, open_count, closed_count, n, choice):
    #     if open_count == n and choice == "(":
    #         return False
    #     if closed_count == n and choice == ")": 
    #         return False
        
    #     stack = []
    #     for c in lst:
    #         if c == "(":
    #             stack.append(c)
    #         elif c == ")" and stack:
    #             stack.pop()
    #         else:
    #             return False
    #     return True

    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def dfs(depth, current_combination, open_count, closed_count, current_stack):
            
            if depth == n * 2:
                current_combination_string = "".join(current_combination) 
                output.append(current_combination_string)
                return

            for choice in ("(", ")"):
                if open_count == n and choice == "(":
                    continue
                if closed_count == n and choice == ")": 
                    continue

                # apply(choice)
                if choice == "(":
                    current_stack.append(choice)
                elif choice == ")" and current_stack:
                    current_stack.pop()
                else:
                    continue
                current_combination.append(choice)
                if choice == "(":
                    open_count += 1
                else:
                    closed_count += 1

                # backtrack(updated state)
                dfs(depth + 1, current_combination, open_count, closed_count, current_stack)
                
                # undo(choice)
                if choice == "(":
                    current_stack.pop()
                elif choice == ")":
                    current_stack.append("(")
                current_combination.pop()
                if choice == "(":
                    open_count -= 1
                else:
                    closed_count -= 1
                

        dfs(0, [], 0, 0, [])
        return output
