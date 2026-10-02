from collections import defaultdict
class Solution:
    def characterReplacement(self, s, k):
        d = defaultdict(list)
        ptrs = defaultdict()
        maxdiff, i, remaining_k = 0, 0 , 0
        freq = defaultdict()
        summer = defaultdict()
        print(s[59: 66])
        letter = "C"

        indexes = [i for i, ch in enumerate(s) if ch == letter]
        print(indexes)
        while i < len(s):
            print(i)
            
            remaining_k = k 
            if s[i] not in d:
                summer[s[i]] = 0
                freq[s[i]] = 1
                starter = i
                while i + 1 != len(s) and s[i] == s[i+1]:
                    freq[s[i]] += 1
                    i +=1
                d[s[i]].append([starter,i])
                ptrs[s[i]] = [starter, i, 0]
                
                
                
                maxdiff = max(maxdiff, i - starter + 1)
            else:
                freq[s[i]] += 1
                d[s[i]].append([i,i])
                index = ptrs[s[i]][2]
                #print("index", index)
                ender = ptrs[s[i]][1] #The last end of the alphabet that worked with i!
                diff = i - ender - 1
                
                summer[s[i]] = 0
                for v, j in enumerate(d[s[i]]):
                    if i == 57:
                        print(d[s[i]])
                    if v - 1 == index: 
                        break
                    else:
                        if j[0] != j[1]:
                            summer[s[i]] += j[1] - j[0] + 1
                        else:
                            summer[s[i]] += 1
                
                print(diff, "=diff")     
                diff -= freq[s[i]] - summer [s[i]] - 1
                print("newdiff =", diff,"freq = ",  freq[s[i]], "sum = ", summer[s[i]])
                
                
                while diff > k: # Here we look at previous starting points and iterate until k is satisfied
                    
                    index = ptrs[s[i]][2]
                    
                        
                    ptrs[s[i]] = [d[s[i]][index + 1][0], d[s[i]][index + 1][1], index + 1]
                    
                    
                    print("sum", summer[s[i]], "index", index, "ptrs", ptrs[s[i]])
                    diff = i - ptrs[s[i]][1] - 1 
                    print(
                            f"i={i}, "
                            f"end={ptrs[s[i]][1]}, "
                            f"gap={i - ptrs[s[i]][1] - 1}, "
                            f"freq={freq[s[i]]}, "
                            f"summer={summer[s[i]]}, "
                            f"active={freq[s[i]] - summer[s[i]] + 1}, "
                            f"diff={i - ptrs[s[i]][1] - 1 - (freq[s[i]] - summer[s[i]] + 1)}"
                        )
                                            
                
                    if diff < 0: #
                        print("diff<0", diff)
                        diff = 0
                    
                remaining_k = k - diff #How many values can we change after changing everything in between ender and i
            
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    freq[s[i]] += 1
                    i+=1
                    maxdiff = max(i - ptrs[s[i]][0] + 1, maxdiff)
                    d[s[i]][-1][1] = i
                else:
                    maxdiff = max(i - ptrs[s[i]][0] + 1, maxdiff)
                    print("consecutive letters", s[i], "mdiff", maxdiff)

            start_var = ptrs[s[i]][0]
            end_var = len(s) - 1
            if remaining_k != 0:
                if start_var >= remaining_k or end_var >= i + remaining_k:
                    maxdiff = max(i - ptrs[s[i]][0] + 1 + remaining_k, maxdiff)
                    print("space", maxdiff)
                else:
                    maxdiff = max(i - ptrs[s[i]][0] + 1 + start_var + end_var - i, maxdiff)
                    print("smol", maxdiff)
            i+= 1
            
        return maxdiff
                




