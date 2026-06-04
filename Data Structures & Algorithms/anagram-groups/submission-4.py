class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        my_dict = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            my_dict[sorted_s].append(s)

        return list(my_dict.values())