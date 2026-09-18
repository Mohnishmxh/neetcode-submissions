class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(start: int, current: List[int], remaining: int):
            if remaining == 0:
                res.append(list(current))
                return

            for i in range(start, len(nums)):
                # Early termination: numbers are sorted, so subsequent elements will also exceed remaining
                if nums[i] > remaining:
                    break

                current.append(nums[i])
                # Pass i (not i + 1) because elements can be reused
                backtrack(i, current, remaining - nums[i])
                current.pop()

        backtrack(0, [], target)
        return res