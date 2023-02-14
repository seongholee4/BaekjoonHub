import sys

T = 3
while (T):
    N = int(input())
    s_ = 0
    for i in range(N):
        s_ += int(sys.stdin.readline())
        
    if s_ > 0:
        print("+")
    elif s_ == 0:
        print("0")
    else:
        print("-")

    T -= 1