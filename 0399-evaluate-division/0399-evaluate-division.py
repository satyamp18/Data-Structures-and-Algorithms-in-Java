class Solution:
    def calcEquation(self, equations, values, queries):

        # Graph banayenge
        graph = {}

        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            value = values[i]

            # a / b = value
            graph.setdefault(a, []).append((b, value))

            # b / a = 1 / value
            graph.setdefault(b, []).append((a, 1 / value))

        # DFS function
        def dfs(current, target, visited):

            # Target mil gaya
            if current == target:
                return 1.0

            visited.add(current)

            for neighbor, weight in graph[current]:

                if neighbor in visited:
                    continue

                result = dfs(neighbor, target, visited)

                if result != -1.0:
                    return weight * result

            return -1.0

        answers = []

        for a, b in queries:

            # Variable exist nahi karti
            if a not in graph or b not in graph:
                answers.append(-1.0)

            else:
                visited = set()
                result = dfs(a, b, visited)
                answers.append(result)

        return answers