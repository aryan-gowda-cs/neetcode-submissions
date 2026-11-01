class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False for i in range(len(s))]
        for i, letter in enumerate(s):
            for word in words:
                length = len(word)
                start = i - length
                if start>= 0:
                    if dp[start]:
                        print("hu")
                        for j in range(start + 1, i + 1):
                            if s[j] != word[j - start -1]:
                                print(s[j], word[j-start -1])
                                break
                        else:
                            dp[i] = True
                elif start == -1:
                    for j in range(0, i + 1):
                        if s[j] != word[j]:
                            break
                    else:
                        dp[i] = True
        print(dp)
        return dp[-1]
        