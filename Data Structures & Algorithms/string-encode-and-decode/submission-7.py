class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        print(encoded_string)
        return encoded_string


    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1;
            print(i, j)
            length = int(s[i:j])
            decoded_str.append(s[j + 1 : j + length + 1])
            i = j + length + 1
        return decoded_str


# ["Hello","World", "5#"] = 5#Hello5#World1#5#