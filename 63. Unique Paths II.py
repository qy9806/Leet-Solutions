class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp=obstacleGrid
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if dp[i][j]==1:
                    dp[i][j]=0
                else:
                    dp[i][j]=1
        # up date the last row and last column to accomodate obstacle
        for x in range(len(dp[i])-2,-1,-1):
            if dp[-1][x]!=0:
                dp[-1][x]=dp[-1][x+1]#update last row
        for y in range(len(dp)-2,-1,-1):
            if dp[y][-1]!=0:
                dp[y][-1]=dp[y+1][-1]
        # do fill up the rest of the grid with the same technique
        for row in range(len(dp)-2,-1,-1):
            for col in range(len(dp[row])-2,-1,-1):
                if dp[row][col]!=0:
                    dp[row][col]=dp[row+1][col]+dp[row][col+1]
        return dp[0][0]
        