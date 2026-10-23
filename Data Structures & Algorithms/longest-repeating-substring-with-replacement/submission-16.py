class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        counter = [0] * 26
        left = 0
        for right in range(len(s)):
            counter[ord(s[right]) - ord('A')] += 1
            while k < (right - left + 1) - max(counter):
                counter[ord(s[left]) - ord('A')] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length

# time: O(n) with n length of s
# space: O(1)


# sliding window
# left and right pointers
# right keeps moving one step at a time, left moves until the window is valid
# what is a windows's validity condition?
# 
# btw which letter must be used for change, it is the one with most occurences, so how will we know which one is the most occured

# substring is valid if there is enough space to change the letters with the most occured letter
# k >= count(letters that are not the most occured)    <=>   k >= length of substring - count(most occured letter)

# XYYX , k = 2 

# AAABABB