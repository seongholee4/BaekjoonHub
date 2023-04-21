# Title: 수 정렬하기 2
# Link: https://www.acmicpc.net/problem/2750
# Bubble sort
# Time: O(N^2)
# Space: O(N)

N = int(input())
arr = list()

for _ in range(N):
    arr.append(int(input()))

for i in range(N):
    for j in range(N-1, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        # the smallest element is moved to the beginning of the list

for i in range(N):
    print(arr[i])

'''
Bubble Sort repeatedly iterates through the list and compares each pair of adjacent elements. 
If the elements are out of order, they are swapped. 
The algorithm continues to iterate through the list until no more swaps are needed.
Input: [2 4 3 1]
step 1: [2 4 3 1] -> [2 4 1 3] -> [2 1 4 3] -> [1 2 4 3]
step 2: [1 2 4 3] -> [1 2 3 4]
Output: [1 2 3 4]
'''