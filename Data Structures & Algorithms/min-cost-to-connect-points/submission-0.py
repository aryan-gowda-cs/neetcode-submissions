import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        # DSU: initially, each point is its own component
        parent = list(range(n))
        rank = [1] * n

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]  # Path compression
                x = parent[x]
            return x

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            # Already connected: adding this edge creates a cycle
            if root_x == root_y:
                return False

            # Union by rank
            if rank[root_x] < rank[root_y]:
                root_x, root_y = root_y, root_x

            parent[root_y] = root_x
            rank[root_x] += rank[root_y]
            return True

        # Generate every possible edge and its Manhattan distance
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                edges.append((cost, i, j))

        # Min-heap: cheapest edges come out first
        heapq.heapify(edges)

        total_cost = 0
        edges_used = 0

        while edges and edges_used < n - 1:
            cost, u, v = heapq.heappop(edges)

            # Accept this edge only if it connects separate components
            if union(u, v):
                total_cost += cost
                edges_used += 1

        return total_cost