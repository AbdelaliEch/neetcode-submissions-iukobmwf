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
            j = i

            while j < len(s) and s[j] != "#":
                j += 1
            
            # print(i, j, s[i:j])

            length = int(s[i:j])

            # print(i, s[i], i + 1, i + int(s[i]) + 1, s[ i + 1 : i + int(s[i]) + 1 ])
            strs.append(s[j + 1 : j + length + 1 ])

            # print(strs)

            i = j + length + 1
           
        # print(strs)
        return strs

# ["Hello","World"] = 5Hello5World

