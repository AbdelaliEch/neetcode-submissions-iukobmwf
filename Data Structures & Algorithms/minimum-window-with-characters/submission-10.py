class Solution:
    def minWindow(self, s: str, t: str) -> str:
        output_range, output_length = [-1, -1], float('inf')
        t_set, t_count, window_count = set(t), defaultdict(int), defaultdict(int)
        for c in t:
            t_count[c] += 1

        letters_found = left = 0
        for right in range(len(s)):
            if s[right] in t_set:
                window_count[s[right]] += 1
                if window_count[s[right]] == t_count[s[right]]:
                    letters_found += 1
                # valid window
                while letters_found == len(t_set):
                    if right - left + 1 < output_length:
                        output_range = [left, right]
                        output_length = right - left + 1

                    if s[left] in t_set:
                        window_count[s[left]] -= 1
                        if window_count[s[left]] < t_count[s[left]]:
                            letters_found -= 1
                    left += 1
        
        left, right = output_range
        return s[left:right + 1] if output_range != [-1, -1] else ""

# time: O(m + n) with m length of t and n length of s
# space: O(k) unique characters of t



# sliding window exercise

# usually the sliding window goes like this:
# window gets initialized as valid, right keeps moving until window is invalid, then we move left until it
# becomes valid again


# in this exercise we will do the opposite:
# window starts as invalid, right keeps moving until window is valid, then we move left until it 
# becomes invalid again