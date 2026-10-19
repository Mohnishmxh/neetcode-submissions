class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def dp(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]
            
            # If pattern reaches the end, string must also reach the end
            if j == len(p):
                return i == len(s)
            
            # Check if the current characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            
            # Handle '*' operator
            if j + 1 < len(p) and p[j + 1] == '*':
                # Option 1: Zero occurrences of preceding element (skip p[j] and p[j+1])
                # Option 2: One or more occurrences (if first_match is true, advance s pointer i)
                ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # Normal match, advance both pointers
                ans = first_match and dp(i + 1, j + 1)
                
            memo[(i, j)] = ans
            return ans

        return dp(0, 0)