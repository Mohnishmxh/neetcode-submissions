class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(open_count: int, close_count: int, current: list[str]):
            # Base case: valid string of length 2 * n formed
            if len(current) == 2 * n:
                res.append("".join(current))
                return

            # Add an opening bracket if quota remains
            if open_count < n:
                current.append("(")
                backtrack(open_count + 1, close_count, current)
                current.pop()

            # Add a closing bracket only if it doesn't exceed open brackets
            if close_count < open_count:
                current.append(")")
                backtrack(open_count, close_count + 1, current)
                current.pop()

        backtrack(0, 0, [])
        return res