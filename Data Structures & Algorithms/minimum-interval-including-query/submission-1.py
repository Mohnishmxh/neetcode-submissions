import bisect
from typing import List


class Solution:

  def minInterval(
      self, intervals: List[List[int]], queries: List[int]
  ) -> List[int]:
    # 1. Sort intervals by length (smallest first)
    intervals.sort(key=lambda x: (x[1] - x[0] + 1))

    # 2. Sort unique queries for binary search
    sorted_unique_queries = sorted(list(set(queries)))
    m = len(sorted_unique_queries)

    # 3. DSU parent array: parent[i] points to the next unanswered query index
    parent = list(range(m + 1))

    def find(i: int) -> int:
      path = []
      while parent[i] != i:
        path.append(i)
        i = parent[i]
      for node in path:
        parent[node] = i
      return i

    # Map each unique query to its answer
    ans_map = {}

    for left, right in intervals:
      length = right - left + 1

      # Find first query >= left
      idx = bisect.bisect_left(sorted_unique_queries, left)
      idx = find(idx)

      # Assign length to all unanswered queries <= right
      while idx < m and sorted_unique_queries[idx] <= right:
        ans_map[sorted_unique_queries[idx]] = length
        parent[idx] = idx + 1  # Union with next index
        idx = find(idx)

    # Reconstruct answers in original query order
    return [ans_map.get(q, -1) for q in queries]