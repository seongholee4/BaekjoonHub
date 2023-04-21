# Title: 수 정렬하기 2
# Link: https://www.acmicpc.net/problem/2750
# selection sort
# Time: O(N^2)
# Space: O(N)

N = int(input())
unsorted = list()

for _ in range(N):
    unsorted.append(int(input()))

for i in range(N):
    min = i
    for j in range(i+1, N):
        if unsorted[min] > unsorted[j]:
            min = j
    temp = (unsorted[min], unsorted[i])
    # unsorted[i], unsorted[min] = temp
    unsorted[i] = temp[0]
    unsorted[min] = temp[1]
    # Swap takes O(1)
    # unsorted[i], unsorted[min] = unsorted[min], unsorted[i]


for i in range(N):
    print(unsorted[i])

'''
In Selection Sort, the algorithm divides the list into a sorted and an unsorted section.
Initially, the sorted section is empty. In each iteration, the algorithm finds the smallest (or largest, depending on the order)
element in the unsorted section and swaps it with the first unsorted element,
effectively moving it to the end of the sorted section.
The process continues until the entire list is sorted
Input: [2 4 3 1]
step 1: [2 4 3 1] -> [1 4 3 2] -> [1 2 3 4]
Output: [1 2 3 4]
'''