class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = max(piles)
        minimum = 1
        min_k = float('inf')
        while minimum <= maximum:
           
            mid = minimum + (maximum - minimum)//2
            print(minimum, mid, maximum, min_k)
            total_hours = 0
            for no in piles:
                total_hours += math.ceil(no/mid)
            if total_hours > h:
                
                minimum = mid + 1
            else:
                min_k = min(min_k, mid)
                maximum = mid - 1
                
        return min_k

            
        