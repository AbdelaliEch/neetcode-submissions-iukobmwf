class Solution:

    def encode(self, strs: List[str]) -> str:
        s = []
        for word in strs:
            s.append(str(len(word)))
            s.append("#")
            s.append(word)
        return "".join(s)


# time: O(m + n) with n number of strings and m sum of length of all the strings
# space: O(m + n)


    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1 + length
            strs.append(s[j + 1 : i])
        return strs


# time: O(m + n) with n number of strings and m sum of length of all the strings
# space: O(m + n)