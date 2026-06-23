class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a=0
        b=0
        for i in nums:
            if i==0:
                b=0
            else:
                b+=1
            if a<b:
                a=b
        return a