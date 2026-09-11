import collections

class TimeMap:

    def __init__(self):
        # Map key to a list of [timestamp, value] pairs
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
            
        values = self.store[key]
        left, right = 0, len(values) - 1
        res = ""
        
        # Binary search for the largest timestamp <= target timestamp
        while left <= right:
            mid = left + (right - left) // 2
            
            if values[mid][0] <= timestamp:
                res = values[mid][1]  # Valid candidate, record it
                left = mid + 1        # Try to find a closer, larger timestamp
            else:
                right = mid - 1       # Timestamp is too large, look left
                
        return res