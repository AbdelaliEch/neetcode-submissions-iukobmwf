class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def dfs(current_combination, open_count, closed_count):
            if open_count == closed_count == n:
                output.append("".join(current_combination))
                return

            for choice in ("(", ")"):
                if choice == "(" and open_count == n :
                    continue
                if choice == ")" and closed_count == open_count:
                    continue
                
                current_combination.append(choice)
                if choice == "(":
                    open_count += 1
                else:
                    closed_count += 1

                dfs(current_combination, open_count, closed_count)
                
                current_combination.pop()
                if choice == "(":
                    open_count -= 1
                else:
                    closed_count -= 1
    
        dfs([], 0, 0)
        return output

# time: O()
# space: O()