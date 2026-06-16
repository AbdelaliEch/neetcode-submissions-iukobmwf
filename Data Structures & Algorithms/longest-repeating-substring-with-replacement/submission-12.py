class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, len(s)
        freq_count = defaultdict(int)
        res = 0


        for r in range(len(s)):
            freq_count[s[r]] += 1

            while k < (r - l + 1) - max(freq_count.values()):
                freq_count[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))

        return res




# use fucking max, max of a fucking O(26)= O(1) because there are at most 26 chars