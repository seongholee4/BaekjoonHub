T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    s = "Case #"+str(i+1)+": "
    print(s, end="")
    print(A+B)
