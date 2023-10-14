import sys
input = sys.stdin.readline

class P11659_구간합구하기():
    def __init__(self, N: int) -> None:
        self.P_SUM = [0*(N+1)]

    def 구간합(self, N: int, arr: list) -> None:
        self.P_SUM[0] = arr[0]
        for i in range(1, N):
            self.P_SUM.append(arr[i]+self.P_SUM[i-1])
            
if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    s = P11659_구간합구하기(N)
    s.구간합(N, arr)
    for _ in range(M):
        i, j = map(int, input().split())
        if i == 1:
            print(s.P_SUM[j-1])
        else:
            print(s.P_SUM[j-1] - s.P_SUM[i-2])
        

