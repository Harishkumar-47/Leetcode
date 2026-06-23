class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=j=0
        h=len(nums)-1
        while i<=h:
            if nums[i]==0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
            elif nums[i]==1:
                i+=1
            else:
                nums[i],nums[h]=nums[h],nums[i]
                h-=1
