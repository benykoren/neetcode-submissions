class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxs = 0
        subs = ''
        i = 0
        while i < len(s):
            if s[i] not in subs:
                subs += s[i]
                i += 1
            else:
                subs = subs[subs.find(s[i])+1:]
            maxs = max(maxs, len(subs))

        return maxs
        