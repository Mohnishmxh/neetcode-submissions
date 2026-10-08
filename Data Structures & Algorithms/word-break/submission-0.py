from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: empty string
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                # If the prefix s[0...j-1] is valid and s[j...i-1] is a word
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
                    
        return dp[len(s)]