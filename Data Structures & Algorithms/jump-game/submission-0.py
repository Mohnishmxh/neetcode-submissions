class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        for i, jump in enumerate(nums):
            # If the current index is greater than the furthest reachable index, we're stuck
            if i > max_reach:
                return False
            
            # Update the furthest index we can reach
            max_reach = max(max_reach, i + jump)
            
            # If we can already reach or go past the last index, return true
            if max_reach >= len(nums) - 1:
                return True
                
        return True