class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums) + 2)]
        
        for i in range(len(nums)):
            dp[i + 2] = max(dp[i] + nums[i], dp[i + 1])
        print(dp)
        return dp[-1]