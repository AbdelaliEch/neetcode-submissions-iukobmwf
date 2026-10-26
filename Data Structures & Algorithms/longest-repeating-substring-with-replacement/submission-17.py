class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = [0] * 26
        output = 0
        for right in range(len(s)):
            count[ord(s[right]) - ord('A')] += 1
            while k < (right - left + 1) - max(count):
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            output = max(output, right - left + 1)
        return output

# window is valid if k >= length(window) - most_occured_character