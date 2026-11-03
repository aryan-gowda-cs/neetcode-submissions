class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]

        # Base case: amount 0 has exactly one combination
        for j in range(len(coins) + 1):
            dp[0][j] = 1

        for i in range(1, amount + 1):
            for j in range(1, len(coins) + 1):
                coin = coins[j - 1]

                if i - coin < 0:
                    dp[i][j] = dp[i][j - 1]
                else:
                    difference = i - coin
                    dp[i][j] = dp[difference][j] + dp[i][j - 1]

        return dp[amount][len(coins)]