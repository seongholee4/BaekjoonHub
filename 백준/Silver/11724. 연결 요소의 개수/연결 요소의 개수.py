import sys
sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().split())
comp = [set() for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    comp[u].add(v)
    comp[v].add(u)

cnt = 0
visited = set()


'''
1 [2, 5]
2 [1, 5]
5 [2, 1]
3 [4]
4 [3, 6]
6 [4]
'''
def dfs (node: int):
    if node in visited:
        return
    visited.add(node)
    for j in comp[node]:
        if j not in visited:
            dfs(j)

    return

for i in range(1, N+1):
    if i not in visited:
        cnt += 1
        dfs(i)

print(cnt)
