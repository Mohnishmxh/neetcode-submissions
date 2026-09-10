from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        # Frequency of each required character in t
        t_count = Counter(t)
        window_count = {}

        # have: unique characters in current window meeting requirement
        # need: unique characters required from t
        have, need = 0, len(t_count)
        
        # Track the minimum window [start_idx, end_idx]
        res_indices = [-1, -1]
        min_len = float("inf")
        left = 0

        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            # If the current character matches the required count in t
            if char in t_count and window_count[char] == t_count[char]:
                have += 1

            # When the window contains all characters in t, shrink from the left
            while have == need:
                # Update our shortest result if this window is smaller
                window_size = right - left + 1
                if window_size < min_len:
                    min_len = window_size
                    res_indices = [left, right]

                # Remove the leftmost character to find a shorter valid window
                left_char = s[left]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    have -= 1
                left += 1

        start, end = res_indices
        return s[start : end + 1] if min_len != float("inf") else ""


def main():
    solution = Solution()

    # Example 1
    s1, t1 = "OUZODYXAZV", "XYZ"
    print(f'Test 1: "{solution.minWindow(s1, t1)}"')  # Output: "YXAZ"

    # Example 2
    s2, t2 = "xyz", "xyz"
    print(f'Test 2: "{solution.minWindow(s2, t2)}"')  # Output: "xyz"

    # Example 3
    s3, t3 = "x", "xy"
    print(f'Test 3: "{solution.minWindow(s3, t3)}"')  # Output: ""


if __name__ == "__main__":
    main()