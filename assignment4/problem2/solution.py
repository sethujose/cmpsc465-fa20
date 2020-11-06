from __future__ import print_function
import sys

def palindrome(array):
    n = len(array)
    L = [[0 for x in range(n)] for x in range(n)]

    for i in range(n):
        L[i][i] = 1

    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            if array[i] == array[j] and cl == 2:
                L[i][j] = 2
            elif array[i] == array[j]:
                L[i][j] = L[i+1][j-1] + 2
            else:
                L[i][j] = max(L[i][j-1], L[i+1][j]);

    return L[0][n-1]

array = raw_input()
arr = []

for c in array:
    arr.append(ord(c))

print (palindrome(arr))
