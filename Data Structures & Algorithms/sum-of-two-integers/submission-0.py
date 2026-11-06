class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mask to 32 bits to handle Python's arbitrary length integers
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        
        while b != 0:
            # Calculate sum without carries
            sum_without_carry = (a ^ b) & MASK
            # Calculate carries and shift them left
            carry = ((a & b) << 1) & MASK
            
            a = sum_without_carry
            b = carry
            
        # If 'a' is negative (exceeds MAX_INT), decode it back to Python's signed integer
        return a if a <= MAX_INT else ~(a ^ MASK)