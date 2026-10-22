class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Fast C-level early exit: eliminates impossible cases instantly
        if sum(gas) < sum(cost):
            return -1

        start = 0
        current_tank = 0

        # enumerate(zip(...)) avoids repeated index lookups (gas[i], cost[i])
        for i, (g, c) in enumerate(zip(gas, cost)):
            current_tank += g - c
            if current_tank < 0:
                start = i + 1
                current_tank = 0

        return start