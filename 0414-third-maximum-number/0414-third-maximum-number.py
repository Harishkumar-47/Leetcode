class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=set(nums)
        nums=sorted(list(nums))
        a=len(nums)
        if len(nums)<2:
            return nums[a-1]
        else:
            return nums[a-3]
