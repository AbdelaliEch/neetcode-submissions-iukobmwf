class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res, resLen = [-1, -1], float('inf')
        t_chars, s_chars = defaultdict(int), defaultdict(int)
        for c in t:
            t_chars[c] += 1
        
        chars_found = 0
        left = 0
        # print(t_chars)
        for right in range(len(s)):
            if s[right] in t_chars:
                # print("outside", s[left], s[right], dict(s_chars), dict(t_chars))
                s_chars[s[right]] += 1
                if s_chars[s[right]] == t_chars[s[right]]:
                    chars_found += 1
            
                while chars_found == len(t_chars):
                    # print("inside", s[left], s[right], dict(s_chars), dict(t_chars), res)
                    if right - left + 1 < resLen:
                        res = [left, right]
                        resLen = right - left + 1
                    # print("inside2", s[left], s[right], dict(s_chars), dict(t_chars), res)
                    
                    if s[left] in t_chars:
                        s_chars[s[left]] -= 1
                        if s_chars[s[left]] < t_chars[s[left]]:
                            chars_found -= 1
                        # print("inside3", s[left], s[right], dict(s_chars), dict(t_chars), res)
                    
                    left += 1
        
        i, j = res
        return s[i:j+1] if res != [-1,-1] else ""
                