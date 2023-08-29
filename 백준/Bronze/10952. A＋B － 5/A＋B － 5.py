A, B = map(int, input().split())
while A != 0 and B != 0:
    if A == 0 and B == 0:
        break
    else:
        print(A+B)
        A, B = map(int, input().split())