import sys
N = int(sys.stdin.readline().strip())

# I want to make N to be 1 using one of the three options:
# 1. N-1
# 2. N/2 if N is even
# 3. N/3 if N is;/p; divisible by 3
# I want to make N to be 1 using the minimum number of operations

# given N, generate possible operations:
# e.g. if 10 then this can be either 9 or 5 after one operation

    # if 9 then this can be either 8 or 3 after one operation
        # if 8 then this can be either 7 or 4 after one operation
        # if 3 then this can be either 2 or 1 after one operation
        # ...
    # if 5 then this can be either 4 or 2 after one operation
        # if 4 then this can be either 3 or 2 after one operation
        # if 2 then this can be either 1 or 1 after one operation
        # ...
# technically, find all paths to 1 and find the shortest path

def x_possibleOperations(node, visited):
    ret = []
    if not visited[node - 1]:
        ret.append(node-1)
    if node % 2 == 0:
        ret.append(node // 2)
    if node % 3 == 0:
        ret.append(node // 3)
    return ret

def bfs(queue, visited):
    while queue:
        node = queue.pop(0)
        if node == 1:
            break
        for i in x_possibleOperations(node, visited):
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[node]+1
                # print(visited)

queue = [N]
visited = [0 for _ in range(N+1)]
bfs(queue, visited)

print(visited[1])