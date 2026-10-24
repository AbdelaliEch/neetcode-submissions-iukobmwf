class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        res, resLen = [-1, -1], float('inf')

        t_chars, window_chars, found_chars_count = {}, {}, 0
        for char in t:
            t_chars[char] = 1 + t_chars.get(char, 0)

        left = 0
        for right in range(len(s)):
            if s[right] in t_chars:

                window_chars[s[right]] = 1 + window_chars.get(s[right], 0)
                if window_chars[s[right]] == t_chars[s[right]]:
                    found_chars_count += 1
            
                # we found a valid window:
                while found_chars_count == len(t_chars):
                    if (right - left + 1) < resLen:
                        res = [left, right]
                        resLen = right - left + 1

                    if s[left] in t_chars:
                        window_chars[s[left]] -= 1
                        if window_chars[s[left]] < t_chars[s[left]]:
                            found_chars_count -= 1
                    left += 1

        if res != [-1, -1]:
            left, right = res
            return s[left:right+1]
        return ""

# time: O(n) with n length s
# space: O(m) with m number of unique characters of t, if we count output then it is O(n)


# we need to track how many letters from t we have in each window of s
# since this is clearly a sliding window algorithm, surely left and right pointers will start from 0        
# right will keep moving until a condition is satisfied, what is this condition?
# here right first needs to move until we find all the t letters
# if i just use a count, it won't work, for example: t = abc , and the window is: aac, the count will show 3 found letters, but we have no b
# so we need to use hashmaps, and compare them each time

# i need to compare by using: t_chars == window_chars
# to make the window valid we do not necessarily need t_chars == window_chars, because window can have multiple occurences of one char
# so we maybe need a count 

# what is next after we find a valid window? it is finally the time to move the left pointer
# but how will it move? left needs to move and shrink as long as the window is valid