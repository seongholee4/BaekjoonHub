import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

L = [[0]*M]*N
for i in range(N):
    line = sys.stdin.readline().strip()
    L[i] = [int(a) for a in line]

cnt = 0
visited = [[False for _ in range(M)] for _ in range(N)]

def find_valid_neighbors(node):
    x, y = node
    ret = []
    # move right
    if (x + 1) < N and L[x + 1][y] == 1:
        ret.append((x+1, y))
    # move left
    if (x - 1) >= 0 and L[x - 1][y] == 1:
        ret.append((x-1, y))
    # move down
    if (y - 1) >= 0 and L[x][y - 1] == 1:
        ret.append((x, y-1))
    # move up
    if (y + 1) < M and L[x][y + 1] == 1:
        ret.append((x, y+1))

    return ret



queue = []
# l = [[0 for _ in range(M)] for _ in range(N)]
queue.append((0, 0, 1))
visited[0][0] = True
while queue:
    node = queue.pop(0)
    x, y, d = node  # coordinates x, y
    if (x, y) == (N-1,M-1):
        print(d)
        break
    if L[x][y] == 1:
        for _x, _y in find_valid_neighbors((x,y)):
            # print(f"node: {node} ... _x, _y: {(_x,_y)}")
            if not visited[_x][_y]:
                # print(f"append: {_x, _y}")
                queue.append((_x,_y, d+1))
                visited[_x][_y] = True
                # l[_x][_y] = d+1

# print(l)
'''
2 2
10
11
'''
