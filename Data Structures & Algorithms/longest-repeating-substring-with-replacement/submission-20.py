class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        left = 0
        count = [0] * 26
        for right in range(len(s)):
            count[ord(s[right]) - ord('A')] += 1
            while k < (right - left + 1) - max(count):
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength

# time: O(n)
# space: O(1)