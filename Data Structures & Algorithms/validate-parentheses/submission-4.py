class Solution:
    def isValid(self, s: str) -> bool:
        open_of_closed = {")":"(", "}":"{", "]":"["}
        stack = []


        for c in s:
            if c in open_of_closed:
                if not stack or open_of_closed[c] != stack[-1]:
                    return False
                last = stack.pop()
            else:
                stack.append(c)
        if stack:
            return False
        return True

# space: O(n)
# time: O(n)
