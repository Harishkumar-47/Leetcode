class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=0
        a=0
        r=nums
        nums=set(nums)
        for i in nums:
            if a < r.count(i):
                n=i
                a= r.count(i)
        return n