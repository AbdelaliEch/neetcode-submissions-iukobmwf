class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for s in strs:
            output.append(str(len(s)))
            output.append("#")
            output.append(s)
        return "".join(output)


    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            output.append(s[j+1:j+1+length])
            i = j+1+length
        return output


