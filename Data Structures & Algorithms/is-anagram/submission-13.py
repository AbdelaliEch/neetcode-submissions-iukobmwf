class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = [0] * 26 
        c2 = [0] * 26  

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            ltidx1 = ord(s[i].lower()) - ord('a')
            ltidx2 = ord(t[i].lower()) - ord('a')            
            c1[ltidx1] += 1  
            c2[ltidx2] += 1

        return c1 == c2

# time: O(n)
# space: O(1)