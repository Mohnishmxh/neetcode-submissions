class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses: list[int]) -> int:
            prev2, prev1 = 0, 0
            for money in houses:
                prev2, prev1 = prev1, max(prev1, prev2 + money)
            return prev1

        # Case 1: Exclude the last house (nums[:-1])
        # Case 2: Exclude the first house (nums[1:])
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))