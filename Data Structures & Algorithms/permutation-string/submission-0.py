from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        
        # If s1 is longer than s2, a permutation cannot fit inside s2
        if len1 > len2:
            return False

        # Frequency count of s1 and the first window of s2
        s1_count = Counter(s1)
        window_count = Counter(s2[:len1])

        # Check the first window
        if s1_count == window_count:
            return True

        # Slide the window across s2
        for i in range(len1, len2):
            # Add the new character entering the window
            window_count[s2[i]] += 1

            # Remove the oldest character leaving the window
            old_char = s2[i - len1]
            window_count[old_char] -= 1
            if window_count[old_char] == 0:
                del window_count[old_char]

            # Compare window frequencies with s1 frequencies
            if window_count == s1_count:
                return True

        return False


def main():
    # Instantiate the Solution class
    solution = Solution()

    # Example 1
    s1 = "abc"
    s2 = "lecabee"
    print(f"Test 1: {solution.checkInclusion(s1, s2)}")  # Expected: True

    # Example 2
    s1 = "abc"
    s2 = "lecaabee"
    print(f"Test 2: {solution.checkInclusion(s1, s2)}")  # Expected: False


if __name__ == "__main__":
    main()