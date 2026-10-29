
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = [gas[i] - cost[i] for i in range(len(gas))]

        if sum(diff) < 0:
            return -1

        tank = 0
        start = 0

        for i in range(len(diff)):
            tank += diff[i]

            if tank < 0:
                start = i + 1
                tank = 0

        return start if start < len(gas) else -1
