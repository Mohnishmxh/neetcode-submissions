class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        prev2 = 1
        prev1 = 1

        for i in range(1, len(s)):
            curr_char = s[i]
            prev_char = s[i - 1]
            current = 0

            # Single digit: valid if non-zero
            if curr_char != '0':
                current = prev1

            # Two digits: valid if '10' through '26'
            if prev_char == '1' or (prev_char == '2' and curr_char <= '6'):
                current += prev2

            if current == 0:
                return 0

            prev2, prev1 = prev1, current

        return prev1