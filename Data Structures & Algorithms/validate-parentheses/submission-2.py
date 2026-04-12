class Solution:
    def isValid(self, s: str) -> bool:
        closed_of_open = {"(": ")", "{": "}", "[": "]"}
        stack = []


        for c in s:
            if c in ("(", "{", "["):
                stack.append(c)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if c != closed_of_open[last]:
                    return False
        if stack:
            return False
        return True