class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=[]
        s=0
        for i in range(len(nums)):
            s+=nums[i]
            a.append(s)
        return a