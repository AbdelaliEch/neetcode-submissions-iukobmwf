class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c.lower()) - ord('a')] += 1
            my_dict[tuple(count)].append(s)
        return list(my_dict.values())
