class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(left: int, right: int, deletions_left: int) -> bool:
            if left >= right:
                return True
            if s[left] == s[right]:
                return check(left + 1, right - 1, deletions_left)
            if deletions_left == 0:
                return False
            return (
                check(left + 1, right, deletions_left - 1) or
                check(left, right - 1, deletions_left - 1)
            )

        return check(0, len(s) - 1, 1)