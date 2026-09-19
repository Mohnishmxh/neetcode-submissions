class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        solutions = []
        queens = [-1] * n
        all_ones = (1 << n) - 1

        def backtrack(row: int, cols: int, d1: int, d2: int) -> None:
            if row == n:
                solutions.append([
                    "." * c + "Q" + "." * (n - c - 1) for c in queens
                ])
                return

            # Bits that are 1 represent valid, unattacked columns
            available = ~(cols | d1 | d2) & all_ones

            while available:
                # Isolate the lowest set bit
                bit = available & -available
                available &= available - 1

                col = bit.bit_length() - 1
                queens[row] = col

                backtrack(
                    row + 1,
                    cols | bit,
                    (d1 | bit) << 1,
                    (d2 | bit) >> 1,
                )

        backtrack(0, 0, 0, 0)
        return solutions