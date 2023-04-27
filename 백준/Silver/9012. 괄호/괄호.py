import sys
sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline().strip())

for _ in range(N):
    stack = []
    string = sys.stdin.readline().strip()
    string = list(string)
    if string[0] == ")":
        print("NO")
        continue
    stack.append(string[0])
    flag = False
    for i in range(1, len(string)):
        if string[i] == "(":
            stack.append(string[i])
        else:
            if stack:
                stack.pop()
            elif not stack and string[i] == ")":
                flag = True
                break
                
    
    if stack or flag:
        print("NO")
    else:
        print("YES")