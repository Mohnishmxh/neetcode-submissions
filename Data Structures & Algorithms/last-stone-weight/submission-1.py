class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_weight = max(stones)
        bucket = [0] * (max_weight + 1)
        
        # Populate frequency of each stone weight: O(N)
        for s in stones:
            bucket[s] += 1
            
        first_stone = 0
        curr_weight = max_weight
        
        # Process stones from heaviest to lightest: O(W)
        while curr_weight > 0:
            if bucket[curr_weight] == 0:
                curr_weight -= 1
            elif first_stone == 0:
                # Pairs of identical stones cancel each other out in O(1)
                bucket[curr_weight] %= 2
                if bucket[curr_weight] == 1:
                    first_stone = curr_weight
                    bucket[curr_weight] = 0
                curr_weight -= 1
            else:
                # Smash first_stone with one stone of curr_weight
                bucket[curr_weight] -= 1
                diff = first_stone - curr_weight
                
                # If the difference is larger than curr_weight, it is guaranteed
                # to be the new largest stone in the entire multiset.
                if diff > curr_weight:
                    first_stone = diff
                else:
                    first_stone = 0
                    bucket[diff] += 1
                    
        return first_stone