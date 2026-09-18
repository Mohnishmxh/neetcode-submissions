class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        def backtrack(start: int, current: list[int]):
            # Every valid prefix represents a unique subset
            res.append(list(current))

            for i in range(start, len(nums)):
                # Skip duplicate elements at the same recursion depth
                if i > start and nums[i] == nums[i - 1]:
                    continue

                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return res