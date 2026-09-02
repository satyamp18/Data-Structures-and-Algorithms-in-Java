from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)

        # Reverse sort so we can use pop()
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        result = []

        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)

            result.append(airport)

        dfs("JFK")

        return result[::-1]