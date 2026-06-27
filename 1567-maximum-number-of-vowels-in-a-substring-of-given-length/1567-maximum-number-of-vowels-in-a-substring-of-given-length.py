class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v="aeiou"
        count=0
        m=0
        for i in range(k):
            if s[i] in v:
                count+=1
                m=max(m,count)
        if count==k:
            return count
        else:
            for j in range(k,len(s)):
                if s[j-k] in v:
                    count-=1
                if s[j] in v:
                    count+=1
                    m=max(m,count)
            return m
