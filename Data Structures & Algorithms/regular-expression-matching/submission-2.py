class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        t_len, p_len = len(s), len(p)
        
        # dp[i][j] means whether s[i:] matches p[j:]
        dp = [[False] * (p_len + 1) for _ in range(t_len + 1)]
        
        # Base case: empty string matches empty pattern
        dp[t_len][p_len] = True
        
        # Fill base cases for empty string s with patterns that can match empty (e.g., "a*b*")
        for j in range(p_len - 2, -1, -2):
            if p[j + 1] == '*':
                dp[t_len][j] = dp[t_len][j + 2]
            else:
                break
                
        # Fill the DP table from bottom-up, right-to-left
        for i in range(t_len - 1, -1, -1):
            for j in range(p_len - 1, -1, -1):
                first_match = (p[j] == s[i] or p[j] == '.')
                
                if j + 1 < p_len and p[j + 1] == '*':
                    # Choice 1: Zero occurrences of preceding element (skip p[j] and p[j+1])
                    # Choice 2: One or more occurrences (if first_match, consume s[i] and stay at j)
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    # Normal match: consume both characters
                    dp[i][j] = first_match and dp[i + 1][j + 1]
                    
        return dp[0][0]