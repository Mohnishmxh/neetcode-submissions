class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False

        # Check if the first row contains any zeros
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break

        # Check if the first column contains any zeros
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        # Use the first row and column as markers for the rest of the matrix
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Update the inner matrix elements based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Update the first row if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Update the first column if needed
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0