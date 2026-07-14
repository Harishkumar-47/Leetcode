class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        f={}
        for i in nums:
            f[i]=f.get(i,0)+1
        s=0
        
        m=max(f.values())
        
        for i in f.values():
            if i==m:
                s+=i
        return s