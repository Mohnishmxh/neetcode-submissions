class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        
        # Check flags for first row and column
        first_row_has_zero = not all(matrix[0]) # True if any 0 in row 0
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

        # Use first row and column as markers for the rest of the matrix
        for i in range(1, m):
            row = matrix[i]
            for j in range(1, n):
                if row[j] == 0:
                    row[0] = 0
                    matrix[0][j] = 0

        # Update the inner matrix elements based on markers
        for i in range(1, m):
            row = matrix[i]
            row_zero = row[0] == 0
            # Pre-fetch row[0] check to avoid repeated lookups inside the inner loop
            for j in range(1, n):
                if row_zero or matrix[0][j] == 0:
                    row[j] = 0

        # Update the first row if needed
        if first_row_has_zero:
            matrix[0] = [0] * n

        # Update the first column if needed
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0