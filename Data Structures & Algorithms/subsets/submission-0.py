class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        current_subset = []
        
        def backtrack(start_index: int):
            result.append(list(current_subset))
            for i in range(start_index, len(nums)):
                current_subset.append(nums[i])
                backtrack(i + 1)
                current_subset.pop()
                
        backtrack(0)
        return result