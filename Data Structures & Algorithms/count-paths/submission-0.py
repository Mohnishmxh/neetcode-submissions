class Solution:

  def uniquePaths(self, m: int, n: int) -> int:
    k = min(m - 1, n - 1)
    total_steps = m + n - 2
    ans = 1

    for i in range(1, k + 1):
      ans = ans * (total_steps - k + i) // i

    return ans