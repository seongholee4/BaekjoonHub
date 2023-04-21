# Title: 수 정렬하기 2
# Link: https://www.acmicpc.net/problem/2750
# insertion sort
# Time: O(N^2)
# Space: O(N)

N = int(input())
unsorted = list()

for _ in range(N):
    unsorted.append(int(input()))

for i in range(N):
    temp = unsorted[i]
    for j in range(i, 0, -1):
        if  unsorted[j-1] > temp:
            unsorted[j] = unsorted[j-1]
            unsorted[j-1] = temp
        else:
            break

for i in range(N):
    print(unsorted[i])

'''
Insertion Sort also divides the list into sorted and unsorted sections. 
The algorithm iterates through the unsorted section, and for each element, 
it finds the correct position within the sorted section and inserts it there. 
This is done by shifting the elements in the sorted section to make room for the new element.
Input: [2 4 3 1]
step 1: [2 4 3 1] ->  [2 4 3 1]
step 2: [2 4 3 1] ->  [2 3 4 1]
step 3: [2 3 4 1] ->  [1 2 3 4]
Output: [1 2 3 4]
'''