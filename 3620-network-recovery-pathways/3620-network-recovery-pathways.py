from collections import deque

class Solution:
    def findMaxPathScore(self, edges, online, k):
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        max_cost = 0

        for u, v, w in edges:
            graph[u].append((v, w))
            indegree[v] += 1
            max_cost = max(max_cost, w)

        # Topological sorting
        q = deque()
        deg = indegree[:]

        for i in range(n):
            if deg[i] == 0:
                q.append(i)

        topo = []

        while q:
            u = q.popleft()
            topo.append(u)

            for v, w in graph[u]:
                deg[v] -= 1
                if deg[v] == 0:
                    q.append(v)

        def can_achieve(score):
            INF = float('inf')
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, w in graph[u]:
                    if w < score:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    new_cost = dist[u] + w

                    if new_cost < dist[v]:
                        dist[v] = new_cost

            return dist[n - 1] <= k

        # Binary search for maximum minimum edge cost
        left, right = 0, max_cost
        answer = -1

        while left <= right:
            mid = (left + right) // 2

            if can_achieve(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer