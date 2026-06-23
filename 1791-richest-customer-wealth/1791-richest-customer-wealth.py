class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        a=[]
        for i in range(len(accounts)):
            a.append(sum(accounts[i]))
        return max(a)