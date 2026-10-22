class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_surplus = 0
        current_surplus = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_surplus += diff
            current_surplus += diff

            # Tank drops below zero: reset start candidate
            if current_surplus < 0:
                start = i + 1
                current_surplus = 0

        return start if total_surplus >= 0 else -1