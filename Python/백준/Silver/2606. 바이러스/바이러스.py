# 문제 요약
# 한 컴퓨터가 웜 바이러스에 걸리게 된다면, 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.


nodes = int(input())
edges = int(input())

graph = {i: [] for i in range(1, nodes+1)}

for i in range(edges):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = set()

def dfs(node):
    visited.add(node)
    
    for next_node in graph[node]:
        if(next_node not in visited):
            dfs(next_node)

dfs(1)
print(len(visited) - 1)
