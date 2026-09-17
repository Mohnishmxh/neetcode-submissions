from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        
        # Count how many tasks have the maximum frequency
        max_freq_count = sum(1 for count in freq.values() if count == max_freq)
        
        # Calculate minimum cycles based on idle chunks vs total tasks
        min_cycles = (max_freq - 1) * (n + 1) + max_freq_count
        
        return max(len(tasks), min_cycles)