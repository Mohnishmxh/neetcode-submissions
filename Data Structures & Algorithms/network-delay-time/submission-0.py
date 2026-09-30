from collections import defaultdict
import heapq
from typing import List


class Solution:

  def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    # Build directed graph: u -> list of (v, weight)
    graph = defaultdict(list)
    for u, v, w in times:
      graph[u].append((v, w))

    # Min-heap stores: (current_travel_time, node)
    min_heap = [(0, k)]
    dist = {}

    while min_heap:
      d, u = heapq.heappop(min_heap)

      # Skip if already finalized with a shorter distance
      if u in dist:
        continue
      dist[u] = d

      # Early exit if all nodes have been reached
      if len(dist) == n:
        break

      for v, w in graph[u]:
        if v not in dist:
          heapq.heappush(min_heap, (d + w, v))

    # If any node remains unreachable
    if len(dist) < n:
      return -1

    return max(dist.values())