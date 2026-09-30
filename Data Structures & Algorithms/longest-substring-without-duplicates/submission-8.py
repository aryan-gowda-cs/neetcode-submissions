class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)
        length  = 0
        old = 0
        for i, letter in enumerate(s):
            if letter in d:
                old = max(d[letter] + 1, old)
                #print("h")
            d[letter] = i
            
            #print(i, "-", old, "=", i-old + 1, "for", letter)
            length = max(length, i - old + 1)
      
        return length

        