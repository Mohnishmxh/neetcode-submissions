class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes (character -> TrieNode)
        self.children = {}
        # Flag to mark the end of a complete word
        self.is_end = False


class PrefixTree:
    def __init__(self):
        # Initialize the root with an empty TrieNode
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # Must return True only if it's the end of a stored word
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # Returns True as long as the prefix path exists
        return True