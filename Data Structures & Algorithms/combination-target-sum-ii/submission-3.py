class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return

            # Count occurrences of this number
            j = i
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1

            count = j - i
            num = candidates[i]

            # Take 0, 1, 2, ..., count copies
            for k in range(count + 1):
                dfs(j, cur, total)

                if k < count:
                    cur.append(num)
                    total += num

            # Remove the copies added in this frame
            for _ in range(count):
                if cur and cur[-1] == num:
                    cur.pop()

        dfs(0, [], 0)
        return res