class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        m=[]
        for i in range(len(s)):
            if s[i]==c:
                m.append(i)
        print(m)
        l=[]
        for i in range(len(s)):
            r=999
            for j in range(len(m)):
                
                if abs(i-m[j]) < r:
                    r=abs(i-m[j])
            l.append(r)
        return l
