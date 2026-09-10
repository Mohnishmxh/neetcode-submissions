class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        max_len = 0

        for right, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            max_freq = max(max_freq, count[ch])

           
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len