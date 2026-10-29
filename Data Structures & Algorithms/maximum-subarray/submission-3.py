
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        min_prefix = 0
        max_sum = float('-inf')

        for num in nums:
            prefix += num
            max_sum = max(max_sum, prefix - min_prefix)
            min_prefix = min(min_prefix, prefix)

        return max_sum
