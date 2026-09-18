class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        # Quick pruning: check if board has enough characters to match word
        board_counts = {}
        for r in range(ROWS):
            for c in range(COLS):
                board_counts[board[r][c]] = board_counts.get(board[r][c], 0) + 1

        for ch in word:
            if board_counts.get(ch, 0) == 0:
                return False
            board_counts[ch] -= 1

        # Optimization: reverse word if suffix is rarer than prefix to reduce branching
        if board_counts.get(word[0], 0) > board_counts.get(word[-1], 0):
            word = word[::-1]

        def dfs(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True

            if (
                r < 0
                or r >= ROWS
                or c < 0
                or c >= COLS
                or board[r][c] != word[idx]
            ):
                return False

            # Mark the cell as visited in-place
            temp = board[r][c]
            board[r][c] = "#"

            # Explore 4 orthogonal neighbors
            found = (
                dfs(r + 1, c, idx + 1)
                or dfs(r - 1, c, idx + 1)
                or dfs(r, c + 1, idx + 1)
                or dfs(r, c - 1, idx + 1)
            )

            # Backtrack
            board[r][c] = temp
            return found

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False