class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26
        # print(ord(s[0]) - ord('a'))
        # # print(ord('a'))
        for letter in s:
            count1[ord(letter.lower()) - ord('a')] += 1

        for letter in t:
            count2[ord(letter.lower()) - ord('a')] += 1

        print(count1, count2)
        return count1 == count2
        
        
        