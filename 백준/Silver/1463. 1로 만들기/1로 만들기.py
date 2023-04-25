import sys
sys.setrecursionlimit(10**9)
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

# DP memorization list
# Initialize default values
N = int(input())
DP = [-1 for _ in range(N+1)]
DP[0] = 0
DP[1] = 0

def make_1(n):
    if DP[n] != -1:
        return DP[n]
    
    options = [make_1(n-1)]
    if n % 2 == 0:
        options.append(make_1(n//2))
    if n % 3 == 0:
        options.append(make_1(n//3))

    DP[n] = min(options) + 1
    return DP[n]
'''
if N = 4
then DP[4] = min(DP[3], DP[2], DP[3]) + 1
DP[3] = 1
DP[2] = 1
'''

for i in range(2, N+1):
    make_1(i)

print(make_1(N))