class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # dp[j] will store the number of distinct subsequences of t[0...j-1]
        # optimized from a 2D table to a 1D array since dp[i] only depends on dp[i-1]
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string t can always be formed 1 way
        
        for i in range(1, m + 1):
            # Iterate backwards to use values from the previous row (i-1)
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]