class Solution:
    def isValid(self, s: str) -> bool:
        open_parentheses = {"{", "(", "["}
        closed_to_open = {"}": "{", ")": "(", "]": "["}
        stack = []
        for c in s:
            # print(c, stack)
            if c in open_parentheses:
                stack.append(c)
            elif c in closed_to_open:
                if not stack or stack[-1] != closed_to_open[c]:
                    return False
                stack.pop()
            else:
                continue
        return not stack

# time: O(n)
# space: O(n)

# ([{}])