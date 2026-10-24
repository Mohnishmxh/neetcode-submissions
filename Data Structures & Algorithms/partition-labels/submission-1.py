class Solution:
    def partitionLabels(self,s: str) -> list[int]:
    # Step 1: Find the last position where each character appears
        last_index = {char: i for i, char in enumerate(s)}
    
        result = []
        start = 0
        end = 0
    
    # Step 2: Loop through the string and build partitions
        for i, char in enumerate(s):
            # Extend our current partition's boundary to the last occurrence of the current letter
            end = max(end, last_index[char])
            
            # If our current index has reached the boundary, we've finished a partition!
            if i == end:
                result.append(end - start + 1)  # Calculate the size of the partition
                start = i + 1                   # Move the start pointer for the next partition
                
        return result
        