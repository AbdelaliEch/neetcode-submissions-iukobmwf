class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        # print(count1)
#         print()
        for i in range(len(s2) - len(s1)):
            print(i, count2)
            if count1 == count2:
                return True
            count2[ord(s2[i + len(s1)]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] -= 1
            # print(i, count2)
            # print()
        return count1 == count2

# sliding window
# validity condition:
#   same count


# lecabee
# 4 = 7 - 3
