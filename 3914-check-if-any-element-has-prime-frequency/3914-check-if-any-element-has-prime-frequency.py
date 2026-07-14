class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        f={}
        for i in nums:
            f[i]=f.get(i,0)+1
        a=[]
        c=0
        m=False
        for i in f.values():
            for j in range(1,i+1):
                if j==i:
                    continue
                else:
                    if i%j==0:
                        c+=1
            a.append(c)
            c=0
        print(a)
        for i in a:
            if i==1:
                return True
        return False