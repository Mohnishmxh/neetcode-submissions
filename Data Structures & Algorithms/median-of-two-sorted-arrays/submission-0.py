class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to optimize the binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        total_left = (m + n + 1) // 2
        
        while left <= right:
            i = (left + right) // 2
            j = total_left - i
            
            # Boundary checks using negative/positive infinity
            max_left_1 = nums1[i - 1] if i > 0 else float('-inf')
            min_right_1 = nums1[i] if i < m else float('inf')
            
            max_left_2 = nums2[j - 1] if j > 0 else float('-inf')
            min_right_2 = nums2[j] if j < n else float('inf')
            
            # Check if partition is correct
            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                # If total length is odd, median is the max of the left elements
                if (m + n) % 2 == 1:
                    return float(max(max_left_1, max_left_2))
                # If total length is even, median is the average of the two middle elements
                return (max(max_left_1, max_left_2) + min(min_right_1, min_right_2)) / 2.0
            
            elif max_left_1 > min_right_2:
                right = i - 1  # Too many elements from nums1 on the left
            else:
                left = i + 1   # Too few elements from nums1 on the left