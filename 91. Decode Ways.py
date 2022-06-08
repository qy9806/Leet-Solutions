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
            
    def numDecodings(self, s: str) -> int:
        dp=[0]*(len(s)+1)
        if len(s)==0 or int(s[0])==0: return 0
        dp[0]=1
        dp[1]=1

        for x in range(1,len(s)):
            if int(s[x])>0:
                dp[x+1]+=dp[x]
            b=int(s[x-1:x+1])
            if b<27 and b>9:
                dp[x+1]+=dp[x-1]
        
        return dp[-1]   