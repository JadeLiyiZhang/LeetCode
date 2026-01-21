class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        graph = {}

        for x, y in stones:
            row = f"r{x}"
            col = f"c{y}"
            if row not in graph:
                graph[row] = []
            if col not in graph:
                graph[col] = []
            graph[row].append(col)
            graph[col].append(row)

        visited = set()

        def dfs(node):
            stack = [node]
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            stack.append(neighbor)

        components = 0
        for x, y in stones:
            row = f"r{x}"
            if row not in visited:
                dfs(row)
                components += 1

        return len(stones) - components
