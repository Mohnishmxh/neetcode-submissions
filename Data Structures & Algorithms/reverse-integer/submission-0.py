class Solution:

  def reverse(self, x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1

    # Keep track of the sign and work with the absolute value
    sign = -1 if x < 0 else 1
    x = abs(x)
    rev = 0

    while x != 0:
      digit = x % 10
      x //= 10

      # Check if multiplying by 10 and adding the digit will exceed INT_MAX
      if rev > (INT_MAX - digit) // 10:
        return 0

      rev = rev * 10 + digit

    return sign * rev