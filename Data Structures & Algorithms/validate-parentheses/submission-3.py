class Solution:
    def isValid(self, s: str) -> bool:
        open_of_closed = {")":"(", "}":"{", "]":"["}
        stack = []


        for c in s:
            if c in ("(", "{", "["):
                stack.append(c)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if open_of_closed[c] != last:
                    return False
        if stack:
            return False
        return True