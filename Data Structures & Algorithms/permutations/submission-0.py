class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtrack(first: int):
            # All positions have been filled
            if first == len(nums):
                res.append(nums[:])
                return

            for i in range(first, len(nums)):
                # Place nums[i] at the current position 'first'
                nums[first], nums[i] = nums[i], nums[first]
                # Recurse for the next position
                backtrack(first + 1)
                # Backtrack / undo the swap
                nums[first], nums[i] = nums[i], nums[first]

        backtrack(0)
        return res