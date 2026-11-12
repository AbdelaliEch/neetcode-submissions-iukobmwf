class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_count = defaultdict(int)
        for c in t:
            t_count[c] += 1


        res, resLen = [-1, -1], float('inf')

        window_count = defaultdict(int)
        letters_found = 0
        left = 0
        for right in range(len(s)):
            # print("outer loop", left, right, res, resLen)
            if s[right] in t_count:
                window_count[s[right]] += 1
                if window_count[s[right]] == t_count[s[right]]:
                    letters_found += 1
                

                while letters_found == len(t_count):
                    # print("inner loop", left, right, res, resLen)
                    if (right - left + 1) < resLen:
                        res = [left, right]
                        resLen = right - left + 1
                    
                    if s[left] in t_count:
                        window_count[s[left]] -= 1
                        if window_count[s[left]] < t_count[s[left]]:
                            letters_found -= 1
                    
                    left += 1

        left, right = res
        return s[left:right+1] if res != [-1,-1] else ""
                    

            



# sliding window needed

# when is the window valid? if all t letters occur in the s window with same frequency or more, so we need to count letters frequency

# we do not have only lowercase or uppercase chars, so we need a normal counter, not count[26]

# and we cannot compare the two dicts each time, so we need a variable for seeing how many t letters did we found in s so far





# do we start with valid or invalid window? invalid, so at first the right needs to keep going until the window becomes valid
# then we save current res
# and we move the left until the window becomes invalid