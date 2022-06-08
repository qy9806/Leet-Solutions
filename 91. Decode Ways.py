class Solution:
    def numDecodings(self, s: str) -> int:
        #start with base case that dp[0]=1 because if we hit 0, means there's a way to decode
        #set base case dp[1]= 1 if the number is valid
        #start from the second index, if it's valid for one digit, take dp[i-1]
        #if it's valid for two digit take the dp[i-2]
        dp=[0]*(len(s)+1)
        dp[0]=1
        dp[1]=1
        if int(s[0])==0:dp[1]=0
        
        for i in range(2,len(s)+1):
            onedigit=s[i-1]
            twodigit=s[i-2:i]
            if int(onedigit)!=0:dp[i]+=dp[i-1]
            if int(twodigit)<27 and int(twodigit)>9:dp[i]+=dp[i-2]
        print(dp)
        return dp[-1]
            