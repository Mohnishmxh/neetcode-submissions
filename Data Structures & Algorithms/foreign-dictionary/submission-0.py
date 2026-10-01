from collections import deque

class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        # Step 1: Initialize graph and in-degree counts for all unique characters
        adj = {char: set() for word in words for char in word}
        in_degree = {char: 0 for char in adj}

        # Step 2: Compare adjacent words to build directed edges
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # Invalid prefix rule (e.g., ["apple", "app"])
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    u, v = w1[j], w2[j]
                    if v not in adj[u]:
                        adj[u].add(v)
                        in_degree[v] += 1
                    break

        # Step 3: Kahn's Algorithm (BFS topological sort)
        queue = deque([char for char, deg in in_degree.items() if deg == 0])
        order = []

        while queue:
            u = queue.popleft()
            order.append(u)
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        # Step 4: Cycle detection
        if len(order) < len(in_degree):
            return ""

        return "".join(order)