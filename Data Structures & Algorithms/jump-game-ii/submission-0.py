class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        cur_end = 0
        farthest = 0
        # Note: loop stops at len(nums)-1, so we never count a jump from the last index
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == cur_end:          # exhausted the current jump's reach
                jumps += 1
                cur_end = farthest    # next jump extends to 'farthest'
        return jumps