class Solution:
    def majorityElement(self,nums: list[int]) -> list[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            
            if len(counts) == 3:
                # 3 distinct elements: decrement all and drop zeros
                counts = {k: v - 1 for k, v in counts.items() if v > 1}

        threshold = len(nums) // 3
        return [c for c in counts if nums.count(c) > threshold]