class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_count = defaultdict(int)
        count = 0
        l = 0
        for r in range(len(s)):
            freq_count[s[r]] += 1
            # print(l, r)
            while k < (r - l + 1) - max(freq_count.values()):
                print(l, r)
                freq_count[s[l]] -= 1
                l += 1
            count = max(count, r - l + 1)
        return count

