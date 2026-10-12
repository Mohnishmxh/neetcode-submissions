from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # Initial states on day 0
        sold = float('-inf')
        held = -prices[0]
        reset = 0
        
        for price in prices[1:]:
            pre_sold = sold
            sold = held + price
            held = max(held, reset - price)
            reset = max(reset, pre_sold)
            
        return max(sold, reset)