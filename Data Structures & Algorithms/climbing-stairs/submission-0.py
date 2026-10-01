class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2 = 1  # ways(1)
        prev1 = 2  # ways(2)

        for _ in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1