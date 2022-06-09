class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #set the last row and last column to be 1, 
        #since at the last row and last column you only have one way to get to the end
        #then at each grid it can either go to right or down
        #so dp[r][c]=dp[r+1][c]+dp[r][c+1]
        #then return the dp frist grid
        dp=[[1]*n for _ in range(m)]
        for x in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[x][j]=dp[x+1][j]+dp[x][j+1]
        return dp[0][0]