class Solution:
    def combinationSum2(
        self, candidates: list[int], target: int
    ) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(start: int, current: list[int], remaining: int):
            if remaining == 0:
                res.append(list(current))
                return

            for i in range(start, len(candidates)):
                # Early exit: since the array is sorted, larger elements cannot fit
                if candidates[i] > remaining:
                    break

                # Skip duplicates at the same decision level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current.append(candidates[i])
                # Advance to i + 1 because each number can only be picked once
                backtrack(i + 1, current, remaining - candidates[i])
                current.pop()

        backtrack(0, [], target)
        return res