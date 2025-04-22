def dfs(graph, start, n):
    visited = [False] * n
    stack = [start]
    path = []

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            path.append(node + 1)
            for neighbor in reversed(range(n)):
                if graph[node][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)

    return path
