# Title: 수 정렬하기 2
# Link: https://www.acmicpc.net/problem/2750
# Merge sort
# Time: O(NlogN)
# Space: O(N)

N = int(input())
a = list()

for _ in range(N):
    a.append(int(input()))

def merge_sort(a, start, end):
    if start < end:
        mid =  (start + end) // 2
        left = merge_sort(a, start, mid)
        right = merge_sort(a, mid + 1, end)
        merge(a, start, mid, end)

def merge(a, start, mid, end):
    i, j = start, mid+1
    
    while i <= mid and j <= end:
        if a[i] <= a[j]:
            i += 1
        else:
            temp = a[j]
            for k in range(j, i, -1):
                a[k] = a[k-1]
            a[i] = temp
            i += 1
            mid += 1
            j += 1


merge_sort(a, 0, len(a)-1)

for i in range(N):
    print(a[i])

'''
Merge Sort is a divide-and-conquer algorithm. 
It recursively divides the list into two halves until each half has only one element. 
Then, it merges the halves back together by comparing and sorting the elements as they are combined. 
The merging process continues until the entire list is reassembled and sorted.
Input: [2 4 3 1]
step 1: [2 4 3 1] -> [1 4 3 2] -> [1 2 3 4]
Output: [1 2 3 4]
'''