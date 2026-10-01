class Solution:
    def climbStairs(self, n: int) -> int:
        def multiply(A, B):
            return [
                [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
                [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
            ]

        def matrix_pow(M, p):
            res = [[1, 0], [0, 1]]  # Identity matrix
            base = M
            while p > 0:
                if p & 1:
                    res = multiply(res, base)
                base = multiply(base, base)
                p >>= 1
            return res

        # The transformation matrix
        T = [[1, 1], [1, 0]]
        res = matrix_pow(T, n)
        return res[0][0]