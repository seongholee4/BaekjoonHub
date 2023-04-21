import sys

N, M = map(int, sys.stdin.readline().split())
comp = {}
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    comp[u] = comp.get(u, []) + [v]
    comp[v] = comp.get(v, []) + [u]

cnt = 0
visited = set()
stack = []
for i in range(1, N+1):
    if i not in visited:
        cnt += 1
        visited.add(i)
        stack.append(i)
        while stack:
            node = stack.pop()
            for j in comp.get(node, []):
                if j not in visited:
                    visited.add(j)
                    stack.append(j)

print(cnt)