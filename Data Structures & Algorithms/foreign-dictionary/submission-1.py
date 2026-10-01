class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        # -1 indicates the character does not exist in any word
        in_degree = [-1] * 26
        # adj[u] will hold the unique outgoing neighbors
        adj = [[] for _ in range(26)]
        
        # Mark all characters present in the input
        for word in words:
            for ch in word:
                in_degree[ord(ch) - 97] = 0

        total_unique = sum(1 for d in in_degree if d >= 0)

        # Build adjacency graph
        # Bitmask tracks existing edges to avoid duplicate edge additions in O(1)
        has_edge = [0] * 26

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # Invalid prefix condition: e.g., ["abc", "ab"]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for j in range(min_len):
                c1, c2 = ord(w1[j]) - 97, ord(w2[j]) - 97
                if c1 != c2:
                    # Check if directed edge c1 -> c2 already exists via bitmask
                    if not (has_edge[c1] & (1 << c2)):
                        has_edge[c1] |= (1 << c2)
                        adj[c1].append(c2)
                        in_degree[c2] += 1
                    break

        # Collect 0 in-degree nodes into a simple list (simulated queue)
        queue = [i for i in range(26) if in_degree[i] == 0]
        
        # Pointer-based BFS eliminates deque/popleft overhead
        head = 0
        order = []

        while head < len(queue):
            u = queue[head]
            head += 1
            order.append(chr(u + 97))

            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        # If topological order didn't cover all present characters, a cycle exists
        if len(order) < total_unique:
            return ""

        return "".join(order)