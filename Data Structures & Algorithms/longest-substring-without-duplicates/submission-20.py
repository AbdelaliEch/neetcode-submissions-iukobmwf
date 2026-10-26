class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_set = set()
        left = 0
        output = 0
        for right in range(len(s)):
            while chars_set and s[right] in chars_set:
                chars_set.remove(s[left])
                left += 1
            chars_set.add(s[right])
            output = max(output, right - left + 1)
        return output