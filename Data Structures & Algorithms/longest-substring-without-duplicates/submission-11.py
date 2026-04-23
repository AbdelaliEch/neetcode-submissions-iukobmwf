class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        count = 0
        l = 0
        for r in range(len(s)):                
            while s[r] in my_set:
                my_set.remove(s[l])
                l+=1
            my_set.add(s[r])
            count = max(count, len(my_set))
        return count

# time: O(n)
# space: O(m)