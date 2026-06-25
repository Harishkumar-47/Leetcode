class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        m= 0
        ch = set()
        l = 0
        
        for r in range(n):
            if s[r] not in ch:
                ch.add(s[r])
                m = max(m, r - l + 1)
            else:
                while s[r] in ch:
                    ch.remove(s[l])
                    l += 1
                ch.add(s[r])
        
        return m