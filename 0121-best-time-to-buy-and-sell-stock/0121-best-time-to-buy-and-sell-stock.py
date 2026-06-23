class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=float('inf')
        a=0
        for price in prices:
            if price < m:
                m = price
            else:
                a=max(a,price-m) 
        return a
        