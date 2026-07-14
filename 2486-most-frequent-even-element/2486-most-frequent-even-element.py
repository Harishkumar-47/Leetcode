class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        f={}
        for i in nums:
            f[i]=f.get(i,0)+1
        s=[]
        n=[]
        for i,j in f.items():
            if i%2==0:
                s.append(j)
                n.append(i)
        print(s)
        if s==[]:
            return -1
        
        else:
            r=0
            l=0
            k=9999
            for i in s:
                if i>r:
                    r=i
                    k=n[l]
                    l+=1
                elif i==r:
                    if k>n[l]:
                        k=n[l]
                        l+=1
                    else:
                        l+=1
                else:
                    l+=1
            return k

            return r