class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = 1

        for i in range(1,m + 1):
            for j in range(n + 1):

                # Skip s[i]
                dp[i][j] += dp[i-1][j]

                # Use s[i]
                if j < n and s[i -1] == t[j]:
                    dp[i][j + 1] += dp[i -1 ][j]

        # Print DP table
        print("    ", end="")
        print(" ε  ", end="")
        for c in t:
            print(f"{c:^5}", end="")
        print()

        for i in range(m + 1):
            if i == 0:
                print("ε ", end=" ")
            else:
                print(f"{s[i-1]} ", end=" ")

            for j in range(n + 1):
                print(f"{dp[i][j]:^5}", end="")
            print()

        return dp[m][n]