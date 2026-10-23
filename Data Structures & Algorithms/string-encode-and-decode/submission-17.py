class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word)) + "#" + word
        # print(s)
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            # print("i is: ", i)
            j = i
            while s[j] != "#":
                j += 1
            # print("i and j are: ", i, j)
            length = int(s[i:j])
            i = j + 1 + length
            strs.append(s[j + 1 : i])
            # print(strs)
        return strs

