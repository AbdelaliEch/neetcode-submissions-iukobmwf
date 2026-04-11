class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        my_dict1 = {}
        for letter in s:
            if letter in my_dict1:
                my_dict1[letter] += 1
            else:
                my_dict1[letter] = 1

        my_dict2 = {}
        for letter in t:
            # if letter not in my_dict1:
            #     return False
            if letter in my_dict2:
                my_dict2[letter] += 1
            else:
                my_dict2[letter] = 1

        for letter in my_dict1:
            if letter not in my_dict2:
                return False
            elif my_dict1[letter] != my_dict2[letter]:
                return False
        return True
