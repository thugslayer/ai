def dfs(node, visited, adj_matrix, dfs_order):
    visited[node] = True
    dfs_order.append(node)

    for neighbor in range(1, len(adj_matrix)):
        if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
            dfs(neighbor, visited, adj_matrix, dfs_order)

n = int(input("Enter no. of nodes: "))
print("Enter adjacency matrix:")
adj_matrix = [[0] * (n + 1)]

for _ in range(n):
    row = [0] + list(map(int, input().split()))
    adj_matrix.append(row)

start_node = int(input("Enter start node: "))

# DFS
visited = [False] * (n + 1)
dfs_order = []
dfs(start_node, visited, adj_matrix, dfs_order)

print("DFS Traversal Order:", dfs_order)
