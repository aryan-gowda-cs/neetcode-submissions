class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[1] = 1
        dp[0]= 1
        for no in range(2, n + 1):
            dp[no] = dp[no - 2] + dp[no-1] 
            
        print(dp)
        return dp[-1]
                
        