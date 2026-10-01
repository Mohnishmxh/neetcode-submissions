from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
            
        itinerary = []
        
        def dfs(airport: str):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            itinerary.append(airport)
            
        dfs("JFK")
        return itinerary[::-1]