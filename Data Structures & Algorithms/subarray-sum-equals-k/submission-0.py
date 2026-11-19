class Solution:    
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_counts = {0: 1}  
        curr_sum = 0
        total = 0

        for num in nums:
            curr_sum += num
            
            diff = curr_sum - k
            if diff in prefix_counts:
                total += prefix_counts[diff]
                
            prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1

        return total