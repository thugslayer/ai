from collections import deque

def bfs(n, adj_matrix, start):
    visited = [False] * (n + 1)
    queue = deque()
    bfs_order = []

    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()
        bfs_order.append(node)

        for neighbor in range(1, n + 1):
            if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

    return bfs_order

n = int(input("Enter no. of nodes: "))
print("Enter adjacency matrix:")
adj_matrix = [[0] * (n + 1)]

for i in range(1, n + 1):
    row = [0] + list(map(int, input().split()))
    adj_matrix.append(row)

start_node = int(input("Enter start node: "))

result = bfs(n, adj_matrix, start_node)
print("BFS Traversal Order:", result)
