from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        bits = 1  # sum 0 is reachable
        
        for x in nums:
            bits |= bits << x
            # Check if target-th bit is set
            if (bits >> target) & 1:
                return True
                
        return bool((bits >> target) & 1)