class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        length = left = 0
        for right in range(len(s)):
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            my_set.add(s[right])
            length = max(length, right - left + 1)
        return length