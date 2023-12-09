import sys

n1 = int(sys.stdin.readline())
n2 = sys.stdin.readline()

j = 0
sum = 0
for i in range(2, -1, -1):
    print(n1 * int(n2[i]))
    sum += (n1 * int(n2[i])) * 100/(10**i) # 1 10 100
    j+=1
print(int(sum))