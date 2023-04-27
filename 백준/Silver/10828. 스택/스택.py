import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline().strip())

stack = []
for _ in range(N):
    line = sys.stdin.readline().split()

    if len(line) == 2: # push
        command = line[0]
        num = int(line[1])
        stack.append(num)
    else:
        command = line[0]
        if command == "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)
        if command == "size":
            print(len(stack))
        if command == "empty":
            if stack:
                print(0)
            else:
                print(1)
        if command == "top":
            if stack:
                print(stack[len(stack)-1])
            else:
                print(-1)