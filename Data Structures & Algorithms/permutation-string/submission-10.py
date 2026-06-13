class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        s2_sub_count = [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_sub_count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1_count[i] == s2_sub_count[i]:
                matches += 1
        
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # growing window to len(s1) + 1 from the right
            index = ord(s2[right]) - ord('a')
            s2_sub_count[index] += 1
            # there is new match
            if s1_count[index] == s2_sub_count[index]:
                matches += 1
            # there was a match one stop ago,
            # but no more after adding +1 to s2_sub_count[index]
            elif s1_count[index] + 1 == s2_sub_count[index]:
                matches -= 1


            # shrinking window from the left
            index = ord(s2[left]) - ord('a')
            s2_sub_count[index] -= 1
            if s1_count[index] == s2_sub_count[index]:
                matches += 1
            elif s1_count[index] -1 == s2_sub_count[index]:
                matches -= 1

            left+=1
        
        return matches == 26


# complexity: O(n) O(n)

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


