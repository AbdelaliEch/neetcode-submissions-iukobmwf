class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        result = defaultdict(list)
        for s in strs:
            alphabets_count = [0] * 26
            for l in s:
                l_index = ord(l) - ord('a')
                alphabets_count[l_index] += 1
            result[tuple(alphabets_count)].append(s)
        return list(result.values())


