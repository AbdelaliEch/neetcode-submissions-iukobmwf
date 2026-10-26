class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        
        for i in range(len(s2) - len(s1)):
            if count2 == count1:
                return True
            print(i, count2, count1)
            count2[ord(s2[i]) - ord('a')] -= 1
            count2[ord(s2[i + len(s1)]) - ord('a')] += 1
        # print(count2, count1, )
        return count2==count1
            