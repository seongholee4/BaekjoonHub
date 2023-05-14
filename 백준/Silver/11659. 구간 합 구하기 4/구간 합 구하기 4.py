import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

S = [0 for _ in range(N+1)]
'''
S[0] -> 0
S[1] -> arr[0]
S[2] -> arr[0] + arr[1]
S[3] -> arr[0] + arr[1] + arr[2]
...
S[N] -> arr[0] + arr[1] + ... + arr[N-1]
'''
for i in range(N+1):
    if i == 0:
        S[i] = 0
    else:
        S[i] = S[i-1] + arr[i-1]
        '''
        S[1] = S[0] + arr[0] -> S[1] = 0 + arr[0] -> S[1] = arr[0]
        S[2] = S[1] + arr[1] -> S[2] = arr[0] + arr[1]
        S[3] = S[2] + arr[2] -> s[3] = arr[0] + arr[1] + arr[2]
        ...
        S[N] = S[N-1] + arr[N-1] -> S[N] = arr[0] + arr[1] + ... + arr[N-1]
        '''

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(S[j] - S[i-1])
