from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        # Store unique lengths of words in the dictionary
        word_lens = {len(w) for w in wordDict}
        
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            # Only check split lengths that actually exist in the dictionary
            for l in word_lens:
                if i - l >= 0 and dp[i - l] and s[i - l:i] in word_set:
                    dp[i] = True
                    break  # Found a valid split for this i, move to next i
                    
        return dp[len(s)]