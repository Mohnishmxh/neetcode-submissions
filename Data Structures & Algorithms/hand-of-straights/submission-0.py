from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # If the total number of cards cannot be evenly divided by groupSize, it's impossible
        if len(hand) % groupSize != 0:
            return False
        
        # Count the frequency of each card
        count = Counter(hand)
        
        # Sort the unique card values
        sorted_keys = sorted(count.keys())
        
        # Greedily form groups starting from the smallest available card
        for key in sorted_keys:
            if count[key] > 0:
                freq = count[key]
                # Check and consume enough cards for a group of `groupSize` consecutive values
                for i in range(groupSize):
                    if count[key + i] < freq:
                        return False
                    count[key + i] -= freq
                    
        return True