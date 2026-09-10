from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # stores indices of elements
        res = []

        for i, val in enumerate(nums):
            # 1. Remove indices that are out of the current window boundary
            if q and q[0] <= i - k:
                q.popleft()

            # 2. Maintain monotonic decreasing order:
            # Pop smaller elements from the right because they can never be the maximum
            while q and nums[q[-1]] < val:
                q.pop()

            # 3. Add the current element's index
            q.append(i)

            # 4. Once we have processed at least k elements, record the maximum
            if i >= k - 1:
                res.append(nums[q[0]])

        return res


def main():
    solution = Solution()

    # Example 1
    nums1 = [1, 2, 1, 0, 4, 2, 6]
    k1 = 3
    print(f"Result: {solution.maxSlidingWindow(nums1, k1)}")  # Output: [2, 2, 4, 4, 6]


if __name__ == "__main__":
    main()