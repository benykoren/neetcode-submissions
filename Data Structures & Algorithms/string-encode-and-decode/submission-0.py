class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#"
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        while len(s) > 0:
            i = 0
            num = ""
            while s[i] != "#":
                num += s[i]
                i += 1
            s = s[i+1:]
            res += [s[:int(num)]]
            s = s[int(num):]
        return res

