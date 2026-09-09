class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Count frequencies using a standard dictionary
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # buckets[i] contains numbers that appear exactly i times
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        # Collect elements starting from the highest possible frequency
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result