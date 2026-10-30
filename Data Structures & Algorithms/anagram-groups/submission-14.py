class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            my_dict[tuple(count)].append(s)
        return list(my_dict.values())

# time: O(n * m) with n number of strs and m length of longest string
# space: O(n)