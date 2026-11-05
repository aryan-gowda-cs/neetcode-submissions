class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        if m < n:
            m, n = n, m
            word1, word2 = word2, word1

        dp = [0] * (n + 1)
        nextDp = [0] * (n + 1)

        # Base case: converting empty word1 to prefixes of word2
        for j in range(n + 1):
            dp[j] = j

        for i in range(1, m + 1):
            nextDp[0] = i

            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    nextDp[j] = dp[j - 1]
                else:
                    nextDp[j] = 1 + min(
                        dp[j],      # Delete
                        nextDp[j - 1],  # Insert
                        dp[j - 1]   # Replace
                    )

            dp = nextDp[:]

        return dp[n]