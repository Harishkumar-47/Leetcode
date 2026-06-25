class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a=[0]*26
        b=[0]*26
        r=[]
        
        if len(s)<len(p):
            return []
        else:
            d=0
            for i in range(len(p)):
                a[ord(s[i])-ord("a")]+=1
                b[ord(p[i])-ord("a")]+=1
            if a==b:
                r.append(d)
            for i in range(len(p),len(s)):
                a[ord(s[i])-ord("a")]+=1
                a[ord(s[i-(len(p))])-ord("a")]-=1
                d+=1
                if a==b:
                    r.append(d)
            return r