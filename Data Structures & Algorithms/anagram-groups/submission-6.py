class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        my_dict = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for lt in s:
                count[ord(lt.lower()) - ord('a')] += 1
            my_dict[tuple(count)].append(s)

        return list(my_dict.values())