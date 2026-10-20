class Solution:

    def encode(self, strs: List[str]) -> str:
        s = []
        for word in strs:
            s.append(str(len(word))) 
            s.append("#")
            s.append(word)
        return "".join(s)
 
# concatentation is not free in python strings, it is with arrays. Time complexity

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + length + 1
            strs.append(s[j + 1 : i ])
            
        return strs


