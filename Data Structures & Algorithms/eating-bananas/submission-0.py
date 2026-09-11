class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        
        while left <= right:
            k = left + (right - left) // 2
            
            # Calculate total hours needed at eating rate k
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k  # Equivalent to math.ceil(p / k)
                
            if hours <= h:
                res = k  # Valid speed, try to find a smaller one
                right = k - 1
            else:
                left = k + 1  # Too slow, need a higher speed
                
        return res