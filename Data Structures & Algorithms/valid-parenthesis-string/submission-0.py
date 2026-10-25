class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0
        
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:  # char == '*'
                low -= 1
                high += 1
                
            # If high is negative, there are too many closing brackets
            if high < 0:
                return False
            
            # low cannot be less than 0
            low = max(0, low)
            
        return low == 0