class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = left = count = 0
        chars_set = set()

        while right < len(s):
            # if s[right] not in chars_set:
            #     chars_set.add(s[right])
            # else:
            while s[right] in chars_set:
                chars_set.remove(s[left])
                left+=1
            chars_set.add(s[right])
            count = max(right - left + 1, count)
            right+=1
        return count


# the window between left and right will contain the substrings