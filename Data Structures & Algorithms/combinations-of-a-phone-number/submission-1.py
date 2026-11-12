class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        output = []

        digits_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, current_combination):
            if i == len(digits):
                output.append("".join(current_combination))
                return

            for letter in digits_letters[digits[i]]:
                current_combination.append(letter)
                dfs(i + 1, current_combination)
                current_combination.pop()


        dfs(0, [])

        return output

# time: O(n * 4**n)
# space: O(n)