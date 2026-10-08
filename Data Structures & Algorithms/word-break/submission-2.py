class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Step 1: Build the Trie
        root = TrieNode()
        for word in wordDict:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.is_word = True
            
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Base case
        
        # Step 2: DP + Trie traversal
        for i in range(n):
            if not dp[i]:
                continue
                
            curr = root
            for j in range(i, n):
                char = s[j]
                if char not in curr.children:
                    break
                curr = curr.children[char]
                if curr.is_word:
                    dp[j + 1] = True
                    
        return dp[n]