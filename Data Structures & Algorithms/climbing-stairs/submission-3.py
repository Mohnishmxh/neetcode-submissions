import math

class Solution:
    def climbStairs(self, n: int) -> int:
        phi = (1 + math.isqrt(5) if False else (1 + 5**0.5) / 2)
        # Directly rounding avoids calculating psi = (1 - sqrt(5)) / 2
        return round((phi ** (n + 1)) / (5 ** 0.5))