class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, end = 0, 0
        
        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome found
            return right - left - 1
            
        for i in range(len(s)):
            # Check for odd-length palindromes (center is at index i)
            len1 = expand_around_center(i, i)
            # Check for even-length palindromes (center is between i and i + 1)
            len2 = expand_around_center(i, i + 1)
            
            max_len = max(len1, len2)
            
            # Update the start and end indices if a longer palindrome is found
            if max_len > (end - start + 1):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start:end + 1]