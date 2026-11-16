from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def sift_down(heap_size: int, root: int) -> None:
            while True:
                largest = root
                left = 2 * root + 1
                right = 2 * root + 2

                # Check if left child exists and is greater than current largest
                if left < heap_size and nums[left] > nums[largest]:
                    largest = left

                # Check if right child exists and is greater than current largest
                if right < heap_size and nums[right] > nums[largest]:
                    largest = right

                # If root is already the largest, heap property holds
                if largest == root:
                    break

                # Swap and continue sifting down
                nums[root], nums[largest] = nums[largest], nums[root]
                root = largest

        # Step 1: Build max-heap in O(n) time
        for i in range(n // 2 - 1, -1, -1):
            sift_down(n, i)

        # Step 2: Extract max elements one by one in O(n log n) time
        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            sift_down(end, 0)

        return nums