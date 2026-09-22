class TrieNode:
    def __init__(self):
        self.children = {}
        # Store the actual word at the end node to easily retrieve it
        self.word = None


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # 1. Build the Trie
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word

        rows, cols = len(board), len(board[0])
        result = set()

        # 2. DFS function to explore the board
        def dfs(r: int, c: int, node: TrieNode):
            char = board[r][c]
            if char not in node.children:
                return

            curr_node = node.children[char]
            # If we found a complete word, add it to our results
            if curr_node.word:
                result.add(curr_node.word)

            # Temporarily mark the current cell as visited
            board[r][c] = '#'

            # Explore all 4 neighboring directions (up, down, left, right)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, curr_node)

            # Backtrack: restore the cell's original character
            board[r][c] = char

        # 3. Start DFS from every cell on the board
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return list(result)