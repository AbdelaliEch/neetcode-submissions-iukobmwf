class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def dfs(depth, current_combination, open_count, closed_count):
            
            if depth == n * 2:
                current_combination_string = "".join(current_combination) 
                output.append(current_combination_string)
                return

            for choice in ("(", ")"):
                if choice == "(" and open_count == n :
                    continue
                # if choice == ")" and closed_count == n: 
                #     continue
                if choice == ")" and closed_count == open_count:
                    continue
                

                # apply(choice)
                current_combination.append(choice)
                if choice == "(":
                    open_count += 1
                else:
                    closed_count += 1

                # backtrack(updated state)
                dfs(depth + 1, current_combination, open_count, closed_count)
                
                # undo(choice)
                current_combination.pop()
                if choice == "(":
                    open_count -= 1
                else:
                    closed_count -= 1
    
        dfs(0, [], 0, 0)
        return output


# instead of using a stack, we can play with open count and close count

# when can we add an open parentheses and when can we add a closed one

# the number of opencount must be equal to closed count at the end

# in the middle, the number of closed count must not exceed the number of open count
