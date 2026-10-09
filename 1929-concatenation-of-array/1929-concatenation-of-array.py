class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        result = []
        for num in nums:
            result.append(num)
        for num in nums:
            result.append(num) 
        return result