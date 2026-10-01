class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # prices[i] stores the minimum cost to reach airport i from src
        prices = [float('inf')] * n
        prices[src] = 0

        # At most k stops means at most k + 1 flights (edges)
        for _ in range(k + 1):
            # Create a copy of prices to avoid using updated values from the current round
            temp = list(prices)
            
            for u, v, price in flights:
                if prices[u] == float('inf'):
                    continue
                if prices[u] + price < temp[v]:
                    temp[v] = prices[u] + price
            
            prices = temp

        return prices[dst] if prices[dst] != float('inf') else -1