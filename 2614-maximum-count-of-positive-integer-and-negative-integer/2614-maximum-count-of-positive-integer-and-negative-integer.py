class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count=0
        ab=0
        for i in nums:
            if i>0:
                count+=1
            elif i<0:
                ab+=1
        return max(count,ab)