class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_dict = {"[":"]", "(":")", "{":"}"}
        for c in s:
            if c in parentheses_dict:
                stack.append(c)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if not parentheses_dict[last] == c:
                    return False
        return not stack

# complexity: O(n) O(n)

# "([{}])"

# stack = [ ( [ { }                  ]


