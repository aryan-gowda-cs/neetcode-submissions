class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex = 0

        for i in range(len(nums)):
            if i > maxIndex:
                return False

            maxIndex = max(maxIndex, i + nums[i])

            if maxIndex >= len(nums) - 1:
                return True

        return True