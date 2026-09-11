class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If the middle element is greater than the rightmost element,
            # the minimum must be in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Otherwise, the minimum is in the left half (including mid).
                right = mid
                
        return nums[left]