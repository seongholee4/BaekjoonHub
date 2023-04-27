import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline().strip())

stack = []
operation = []
input = []
for i in range(N):
     input.append(int(sys.stdin.readline().strip()))
    
idx = 0
for i in range(1, N+1):

    stack.append(i)
    operation.append("+")
    
    while idx < len(input) and stack and input[idx] == stack[-1]:
        stack.pop()
        operation.append("-")
        idx += 1

if stack:
    print("NO")
else:
    for i in operation:
        print(i)