class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}
        for letter in s1:
            if letter not in d:
                d[letter] = 1
            else:
                d[letter] += 1
        
        l,r = 0,0 
        temp = d.copy()
        while l < len(s2):
            letter = s2[l]
            if letter in d:
                count = 0
                r = l
                while r - l + 1 <= len(s1) and r < len(s2):
                    print(l,r)
                    letter = s2[r]
                    if letter not in d:
                        break
                    d[letter] -= 1
                    if d[letter] == 0:
                        count += 1
                        if count == len(d):
                            return True
                    elif d[letter] == -1:
                        while s2[l] != letter:
                            if d[s2[l]] == 0:
                                count -= 1
                            d[s2[l]] += 1
                            l += 1
                        
                        l += 1
                        d[letter] = 0
                    r += 1
            while (l != r):
                if s2[l] in d:
                    d[s2[l]] += 1
                l += 1
            l += 1
            r += 1
                    

        return False

                

        