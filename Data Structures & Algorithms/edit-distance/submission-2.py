class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        if m < n:
            m, n = n, m
            word1, word2 = word2, word1

        dp = [i for i in range(n + 1)]

        for i in range(1, m + 1):
            prev = dp[0]
            dp[0] = i

            for j in range(1, n + 1):
                temp = dp[j]

                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = 1 + min(
                        dp[j],      # Delete (old dp[j])
                        dp[j - 1],  # Insert (new dp[j-1])
                        prev        # Replace (old dp[j-1])
                    )

                prev = temp

        return dp[n]