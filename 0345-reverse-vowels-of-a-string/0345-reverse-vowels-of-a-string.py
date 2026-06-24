class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        i=0
        j=len(s)-1
        a="aeiouAEIOU"
        while i<j:
            if s[i] not in a :
                i+=1
            elif s[j] not in a:
                j-=1
            else:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        s="".join(s)
        return s