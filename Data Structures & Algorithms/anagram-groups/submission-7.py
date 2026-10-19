class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        output = []
        
        for s in strs:
            c = [0] * 26
            for l in s:
                c[ord(l.lower()) - ord('a')] += 1
            my_dict[tuple(c)].append(s)
        
        return list(my_dict.values())

    