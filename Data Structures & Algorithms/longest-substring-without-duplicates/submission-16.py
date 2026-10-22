class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        max_length = 0
        left = 0
        for right in range(len(s)):
            # print(left, right, s[left], s[right],  max_length, my_set)
            while s[right] in my_set:
                
                # print(my_set, s[left])
                my_set.remove(s[left])
                # print(my_set)
                left += 1
            
            my_set.add(s[right])
            length = right - left + 1
            max_length = max(max_length, length)
            # print(left, right ,s[left], s[right],  max_length, my_set)
            # print()
        # length = right - left + 1
        # max_length = max(max_length, length)
        return max_length



# sliding window problem
# right and left pointers, right keeps moving each iteration, left moves until the window's condition is valid
# in this case, the window's condiiton is: substring without duplicate characters
# we will need a set

# each iteration, a new letter gets added to the substring/set
# but before adding it, we need to make sure it doesn't already exist in the set

# length of the substring is: right - left + 1