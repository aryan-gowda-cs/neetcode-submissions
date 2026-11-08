class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for length in range(1, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                for i in range(l, r + 1):
                    left = nums[l - 1] if l > 0 else 1
                    right = nums[r + 1] if r < n - 1 else 1

                    coins = (
                        (dp[l][i - 1] if i > l else 0) +
                        (dp[i + 1][r] if i < r else 0) +
                        left * nums[i] * right
                    )

                    dp[l][r] = max(dp[l][r], coins)

        return dp[0][n - 1]