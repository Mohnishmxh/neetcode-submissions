class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        # Transform string: "aba" -> "^#a#b#a#$"
        # ^ and $ act as sentinel boundaries to eliminate bounds checks.
        t = "^#" + "#".join(s) + "#$"
        m = len(t)
        p = [0] * m

        center = 0
        right = 0
        total_palindromes = 0

        for i in range(1, m - 1):
            i_mirror = 2 * center - i  # Mirror of i around center

            if right > i:
                p[i] = min(right - i, p[i_mirror])

            # Expand around center i
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1

            # Update center and right boundary if expanded beyond right
            if i + p[i] > right:
                center = i
                right = i + p[i]

            # In the transformed string, p[i] // 2 gives the count
            # of original palindromes centered at this position
            total_palindromes += (p[i] + 1) // 2

        return total_palindromes