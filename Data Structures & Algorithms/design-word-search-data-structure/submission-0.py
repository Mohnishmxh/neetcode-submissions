class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes (character -> TrieNode)
        self.children = {}
        # Flag to mark the end of a complete word
        self.is_end = False


class WordDictionary:
    def __init__(self):
        # Initialize the root with an empty TrieNode
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index: int, node: TrieNode) -> bool:
            curr = node
            for i in range(index, len(word)):
                char = word[i]
                
                if char == '.':
                    # If we hit a dot, we must recursively check all possible branches
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
                    
            return curr.is_end

        return dfs(0, self.root)