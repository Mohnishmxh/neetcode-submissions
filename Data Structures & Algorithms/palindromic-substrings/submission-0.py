class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        total_palindromes = 0

        def count_around_center(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(n):
            # Odd-length palindromes (single-character center)
            total_palindromes += count_around_center(i, i)
            # Even-length palindromes (two-character center)
            total_palindromes += count_around_center(i, i + 1)

        return total_palindromes