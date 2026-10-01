class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        prev2 = 0  # dp[i - 2]
        prev1 = 0  # dp[i - 1]

        for c1, c2 in zip(cost[:-1], cost[1:]):
            curr = min(prev1 + c2, prev2 + c1)
            prev2, prev1 = prev1, curr

        # Or equivalently:
        first, second = 0, 0
        for c in cost:
            first, second = second, min(first, second) + c
        return min(first, second)