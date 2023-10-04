N = int(input())

s = list(map(int, input().strip()))

ret = 0
for i in range(N):
    ret += s[i]

print(ret)