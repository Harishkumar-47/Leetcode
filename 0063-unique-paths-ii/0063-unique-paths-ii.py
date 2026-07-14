class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r=len(obstacleGrid)
        c=len(obstacleGrid[0])
        dp=[[0]*c for _ in range(r)]
        dp[0][0]=1
        if obstacleGrid[0][0]==1:
            return 0
        for i in range(r):
            for j in range(c):
                if i==0 and j==0:
                    continue
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                else:
                    dp[i][j]+=dp[i-1][j]+ dp[i][j-1]
        return dp[r-1][c-1]