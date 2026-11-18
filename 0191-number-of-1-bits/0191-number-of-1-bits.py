class Solution:
    def hammingWeight(self, n: int) -> int:
        s=bin(n)
        c=0
        for i in str(s):
            if i=="1":
                c+=1
        return c