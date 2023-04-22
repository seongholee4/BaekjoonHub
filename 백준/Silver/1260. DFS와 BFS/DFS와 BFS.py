import sys
sys.setrecursionlimit(10**6)

N, M, V = map(int, sys.stdin.readline().split())

Q = [[] for _ in range(N+1)]
visited = set()
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    Q[u].append(v)
    Q[v].append(u)

for i in Q:
    i.sort()


dfs_path = []
bfs_path = []

def dfs(node):
    dfs_path.append(node)
    visited.add(node)
    for i in Q[node]:
        if i not in visited:
            visited.add(i)
            dfs(i)

def bfs(node):
    queue = [node]
    visited.add(node)
    while queue:
        node = queue.pop(0)
        bfs_path.append(node)
        for i in Q[node]:
            if i not in visited:
                queue.append(i)
                visited.add(i)





dfs(V)
for i in range(len(dfs_path)):
    print(dfs_path[i], end=' ')

print()
visited.clear()
bfs(V)
for i in range(len(bfs_path)):
    print(bfs_path[i], end=' ')