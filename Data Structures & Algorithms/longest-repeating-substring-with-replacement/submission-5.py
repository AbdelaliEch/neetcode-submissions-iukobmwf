class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freq_count = {}

        left = 0
        for right in range(len(s)):
            freq_count[s[right]] = 1 + freq_count.get(s[right], 0)

            while (right - left + 1) - max(freq_count.values()) > k:
                freq_count[s[left]] -= 1
                left+=1
            
            res = max(res, right - left + 1)
    
        return res
            






# ok so we'll use a variable-size sliding window
# when is it valid
# and when is it invalid

# the window is valid as long as we can make enough changes in the current 
# substring
# and how will we make changes???
# in each substring, we need to count the most frequent letter, and change
# the rest to the letters to it.
# so the validity of the window will be:
# if k >= len(substring) - count(mostFrequentLetter)
# else, invalid


