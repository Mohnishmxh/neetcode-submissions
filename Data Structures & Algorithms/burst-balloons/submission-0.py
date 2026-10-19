class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Pad the array with 1s at both ends
        nums = [1] + nums + [1]
        n = len(nums)
        
        # dp[left][right] represents the max coins obtained by bursting 
        # all balloons between index left and right
        dp = [[0] * n for _ in range(n)]
        
        # Iterate over the length of the sub-array
        for length in range(2, n):
            for left in range(n - length):
                right = left + length
                # Try every balloon k as the *last* one to be burst in this range
                for k in range(left + 1, right):
                    coins = nums[left] * nums[k] * nums[right]
                    coins += dp[left][k] + dp[k][right]
                    dp[left][right] = max(dp[left][right], coins)
                    
        return dp[0][n - 1]