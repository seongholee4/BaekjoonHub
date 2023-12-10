import sys

H, M = sys.stdin.readline().split()
H = int(H)
M = int(M)
 
if M >= 45:
    M = M - 45
else:
    if H == 0:
        H = 23
    else:
        H -= 1
    M = 60-(45-M)
print(H, M)