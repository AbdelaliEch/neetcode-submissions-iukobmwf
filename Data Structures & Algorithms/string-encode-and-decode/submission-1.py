class Solution:

    def encode(self, strs: List[str]) -> str:
        print(f"strs: {strs}")
        if strs == []:
            return str(None)
        elif strs == [""]:
            return ""
        return "-/".join(strs)

    def decode(self, s: str) -> List[str]:
        print(f"s: {s}")
        if s == str(None):
            return []
        elif s == "":
            return [""]
        return s.split("-/")