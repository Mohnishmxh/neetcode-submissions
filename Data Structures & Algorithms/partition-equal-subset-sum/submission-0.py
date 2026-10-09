from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        # If total sum is odd, it cannot be partitioned into two equal subsets
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        # dp[s] will be True if a subset with sum s exists
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            # Traverse backwards to ensure each element is used at most once
            for s in range(target, num - 1, -1):
                if dp[s - num]:
                    dp[s] = True
            if dp[target]:
                return True
                
        return dp[target]