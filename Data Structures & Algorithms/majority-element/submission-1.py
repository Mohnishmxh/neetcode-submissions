class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = {}
        
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
        return max(counts, key=counts.get)  # Outside the loop