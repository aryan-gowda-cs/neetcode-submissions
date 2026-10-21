import collections
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        visit = set()

        for _ in range(n):
            # Find the unvisited node with minimum distance
            node = -1
            for i in range(1, n + 1):
                if i not in visit and (node == -1 or dist[i] < dist[node]):
                    node = i

            # No reachable unvisited node remains
            if node == -1 or dist[node] == float('inf'):
                break

            visit.add(node)

            # Relax outgoing edges
            for nei, weight in edges[node]:
                if nei not in visit:
                    dist[nei] = min(dist[nei], dist[node] + weight)

        answer = max(dist[1:])
        return answer if answer != float('inf') else -1