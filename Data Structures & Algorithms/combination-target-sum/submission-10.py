class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, remaining, subset):
            #print(i,remaining,subset)
            if remaining == 0:
                res.append(subset.copy())
            elif remaining <= 0:
                return
            elif i >= len(nums):
                return
            subset.append(nums[i])
            backtrack(i, remaining - nums[i], subset)
            subset.pop()
            for j in range(i + 1,len(nums)):
                if remaining - nums[j] < 0:
                    break
                subset.append(nums[j])
                backtrack(j, remaining - nums[j], subset)
                subset.pop()

        nums.sort()
        backtrack(0, target, [])
        return res