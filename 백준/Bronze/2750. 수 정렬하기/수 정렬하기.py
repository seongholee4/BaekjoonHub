N = int(input())
arr = list()
for i in range(N):
    arr.append(int(input()))
arr = sorted(arr)
for i in range(N):
    print(arr[i])