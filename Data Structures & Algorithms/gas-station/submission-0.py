class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total fuel is strictly less than total consumption, circuit is impossible
        if sum(gas) < sum(cost):
            return -1

        start_station = 0
        current_tank = 0

        for i in range(len(gas)):
            current_tank += gas[i] - cost[i]

            # If fuel runs out, no station up to i can be the start
            if current_tank < 0:
                start_station = i + 1
                current_tank = 0

        return start_station