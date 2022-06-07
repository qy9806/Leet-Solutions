class Solution:
    def rob(self, nums) -> int:
        #create a dp array, have dp[0] set to nums[0]
        #set dp[1]=max(nums[0],nums[1])
        # start looping from 3rd index, for each house:
        #either take from the previouse house or take the current house + the house 
        #before previous house dp[i-2]
        
        
        if len(nums)==0:return 0
        if len(nums)==1:return nums[0]
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],nums[i]+dp[i-2])
        print(dp)
        return dp[-1]
        
        