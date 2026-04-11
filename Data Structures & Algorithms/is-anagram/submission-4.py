class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        my_dict1, my_dict2 = {}, {}
        
        for i in range(len(s)):
            my_dict1[s[i]] = 1 + my_dict1.get(s[i], 0)
            my_dict2[t[i]] = 1 + my_dict2.get(t[i], 0)

        for letter in my_dict1:
            if my_dict1[letter] != my_dict2.get(letter, 0):
                return False
        return True
