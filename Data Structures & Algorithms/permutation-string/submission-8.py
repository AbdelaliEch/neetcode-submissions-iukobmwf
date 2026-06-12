class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        s2_sub_count = [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_sub_count[ord(s2[i]) - ord('a')] += 1

        # print(s1_count)
        # print(s2_sub_count)
        # print()

        for left in range(len(s2) - len(s1) + 1):
            right = left + len(s1) - 1

            if s1_count == s2_sub_count:
                return True
            # print(left, right, s1, s2[left:right+1])
            # print(s1_count)
            # print(s2_sub_count)
            # print()

            
            s2_sub_count[ord(s2[left]) - ord('a')] -= 1
            if right + 1 < len(s2):          
                s2_sub_count[ord(s2[right + 1]) - ord('a')] += 1
            # print(left, right, s1, s2[left:right+1])
            # print(s1_count)
            # print(s2_sub_count)
            # print()
            # if s1_count == s2_sub_count:
            #     return True
            
        return False


# so this is how we will do it
# ofc we will use a sliding window
# right pointer will move by one each time
# left pointer will be moved only when invalid window
# but when is the window considered invalid??????
# when we reach a letter not in s1 
# but the letter can be in s1 and not with same frequency

# s1 must be inside s2 in any order
# so we need to move the sliding window only by 1 , and its size will be size of s1
# and when we find return true


# i should know the last valid window?? hooow to keep the last valid window


