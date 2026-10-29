
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            diff = cost[i] - gas[i]
            total += diff
            tank += diff

            if tank > 0:
                start = i + 1
                tank = 0

        return -1 if total > 0 else start
