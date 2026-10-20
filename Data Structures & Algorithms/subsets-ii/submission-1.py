class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        unique = set()

        def dfs(i, cur):
            if i == len(nums):
                unique.add(tuple(cur))
                return

            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.pop()

            dfs(i + 1, cur)

        dfs(0, [])

        return [list(subset) for subset in unique]