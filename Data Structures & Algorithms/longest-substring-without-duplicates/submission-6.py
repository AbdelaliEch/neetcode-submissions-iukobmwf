class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # my_set = set()
        # count = 0
        # for l in s:
        #     if l not in my_set:
        #         my_set.add(l)
        #     else:
        #         count = max(count, len(my_set))
        #         my_set.clear()
        #         my_set.add(l)
        # count = max(count, len(my_set))
        # return count
        my_set = set()
        count = 0
        for i, l in enumerate(s):
            for il in s[i:]:
                # print(my_set)
                if il not in my_set:
                    my_set.add(il)
                else:
                    count = max(count, len(my_set))
                    # print(count, my_set)
                    my_set.clear()
                    break
            # count = max(count, len(my_set))
        count = max(count, len(my_set))
        return count
