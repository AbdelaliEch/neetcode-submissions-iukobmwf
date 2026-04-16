class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            alphabets_count = [0] * 26
            for l in s:
                l_index = ord(l) - ord('a')
                alphabets_count[l_index] += 1
            result[tuple(alphabets_count)].append(s)
        return list(result.values())



# time: O(n * m) : n is number of strings, m is length of the longest string
# space: O(n): n is number of strings, because in worst case we will have no anagrams
# the list is O(26) = O(1) cuz it gets overwritten