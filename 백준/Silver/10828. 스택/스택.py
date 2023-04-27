import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline().strip())

def push(x):
    stack.append(x)

def pop() -> int:
    if stack:
        return stack.pop()
    else:
        return -1

def size() -> int:
    return len(stack)

def empty() -> int:
    return 0 if stack else 1

def top() -> int:
    return stack[len(stack)-1] if not empty() else -1 

stack = []
for _ in range(N):
    line = sys.stdin.readline().split()
    command = line[0]
    if command == "push":
        push(line[1])
    if command == "pop":
        print(pop())
    if command == "size":
        print(size())
    if command == "empty":
        print(empty())
    if command == "top":
        print(top())
        
