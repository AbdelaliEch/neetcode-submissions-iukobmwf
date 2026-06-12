class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        count = 0
        chars_set = set()

        for right in range(len(s)):
            while s[right] in chars_set:
                chars_set.remove(s[left])
                left+=1
            chars_set.add(s[right])
            count = max(count, right - left + 1)
        return count

# complexity: O(n) O(m)
# the window between left and right will contain the substrings