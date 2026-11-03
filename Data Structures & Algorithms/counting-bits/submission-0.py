class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            # ans[i] is the number of 1s in i >> 1 plus the last bit (i & 1)
            ans[i] = ans[i >> 1] + (i & 1)
        return ans