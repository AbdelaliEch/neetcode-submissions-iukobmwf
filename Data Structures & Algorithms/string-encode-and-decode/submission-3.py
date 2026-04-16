class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return str(None)
        elif strs == [""]:
            return ""
        return "-/".join([string.encode().hex() for string in strs])

    def decode(self, s: str) -> List[str]:
        if s == str(None):
            return []
        elif s == "":
            return [""]
        return [bytes.fromhex(string).decode() for string in s.split("-/")]


