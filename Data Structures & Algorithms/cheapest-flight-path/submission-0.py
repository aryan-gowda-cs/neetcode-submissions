from typing import List

class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        INF = float('inf')
        dp = [[INF] * (k + 2) for _ in range(n)]
        dp[src][0] = 0

        for stops in range(k + 1):
            for u, v, price in flights:
                if dp[u][stops] != INF:
                    dp[v][stops + 1] = min(
                        dp[v][stops + 1],
                        dp[u][stops] + price
                    )

        ans = min(dp[dst])
        return ans if ans != INF else -1