class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(s)
        a.sort()
        b = list(t)
        b.sort()
        a = str(a)
        b = str(b)
        return a == b
        