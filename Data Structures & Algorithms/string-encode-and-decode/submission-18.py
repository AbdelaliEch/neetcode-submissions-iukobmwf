class Solution:

    def encode(self, strs: List[str]) -> str:
        s = []
        for word in strs:
            s.append(str(len(word)))
            s.append("#")
            s.append(word)
            # s += str(len(word)) + "#" + word
        return "".join(s)


# time: O(n) with n number of strings
# space: O(m) with m sum of length of all the strings


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

# time: O()
# space: O()
