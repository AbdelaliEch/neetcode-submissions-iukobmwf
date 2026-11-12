class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        output = []

        digits_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
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

