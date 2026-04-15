class Solution:
    def isAnagram_in_lst(self, s, l):
        for string in l:
            if sorted(string) == sorted(s):
                return True
        return False

    def is_s_in_lists(self, s, l):
        for lst in l:
            if s in l:
                return True
        return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        for s in strs:
            if not self.is_s_in_lists(s, result):
                for lst in result:
                    if self.isAnagram_in_lst(s, lst):
                        lst.append(s)
                        break
                else:
                    result.append([s])

        return result 

