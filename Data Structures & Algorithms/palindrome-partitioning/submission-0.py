class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []

        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def backtrack(start: int, path: list[str]):
            # Base case: reached the end of the string
            if start == len(s):
                res.append(list(path))
                return

            for end in range(start + 1, len(s) + 1):
                prefix = s[start:end]
                if is_palindrome(prefix):
                    path.append(prefix)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return res