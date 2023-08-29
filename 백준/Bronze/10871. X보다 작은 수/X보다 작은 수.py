import sys

N, X = map(int, sys.stdin.readline().split())

class Solution:
    def BOJ10871(self, N: int, X: int):
        arr = map(int, sys.stdin.readline().split())
        for n in arr:
            if n < X:
                print(n, end=" ")
            


s = Solution()
s.BOJ10871(N, X)