from collections import deque

n, m, v = map(int, input().split())

graph = {i : [] for i in range(1, n+1)}

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    graph[i].sort()

dfs_visited = []
def dfs(node):
    if(node not in dfs_visited):
        dfs_visited.append(node)
    
    for next_node in graph[node]:
        if next_node not in dfs_visited:
            dfs(next_node)


bfs_queue = deque()
bfs_visited = []

def bfs(start):
    bfs_queue.append(start)
    bfs_visited.append(start)

    while bfs_queue:
        node = bfs_queue.popleft()

        for next_node in graph[node]:
            if next_node not in bfs_visited:
                bfs_visited.append(next_node)
                bfs_queue.append(next_node)
    
    
dfs(v)
bfs(v)

print(*dfs_visited)
print(*bfs_visited)
