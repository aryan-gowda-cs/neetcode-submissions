
from collections import deque
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        queue = deque([0])
        jumps = 0
        last_used = 0
        while queue:
            i = queue.popleft()

            if i >= len(nums) - 1:
                return jumps

            farthest = i
            best_index = i
            if nums[i] + i >= len(nums) - 1:
                return jumps + 1
                
            for j in range(last_used + 1, min(i + nums[i], len(nums) - 1) + 1):
                if j + nums[j] > farthest + nums[farthest]:
                    farthest = j
                    best_index = j

            if best_index == i:
                best_index = min(i + nums[i], len(nums) - 1)

            queue.append(best_index)
            last_used = best_index
            jumps += 1

        return jumps
