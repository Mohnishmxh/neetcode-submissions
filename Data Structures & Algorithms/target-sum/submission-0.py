class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        # If target is out of reachable bounds or (target + total_sum) is odd, no valid partition exists
        if abs(target) > total_sum or (target + total_sum) % 2 != 0:
            return 0
        
        subset_sum = (target + total_sum) // 2
        
        # dp[j] represents the number of ways to pick a subset that sums to j
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # Base case: 1 way to make sum 0 (empty subset)
        
        for num in nums:
            # Traverse backwards from subset_sum down to num to avoid reusing the same element
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
                
        return dp[subset_sum]