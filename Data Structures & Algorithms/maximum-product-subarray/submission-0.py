class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_so_far = nums[0]
        current_max = nums[0]
        current_min = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            if num < 0:
                current_max, current_min = current_min, current_max
                
            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)
            
            max_so_far = max(max_so_far, current_max)
            
        return max_so_far