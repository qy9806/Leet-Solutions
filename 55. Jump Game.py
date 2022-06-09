class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #bottom up memoization
        #keep updating the current target
        target=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=target:
                target=i
        return target==0