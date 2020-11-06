from __future__ import print_function
import sys

def merge_two_sorted_arrays(arr1, arr2):
    output = []
    Ka = Kb = 0

    len1 = len(arr1)
    len2 = len(arr2)
    if ((len1 == 0) and (len2 == 0)):
        return output
    if (len1 == 0):
        for i in range(0, len2):
            output.append(arr2[i])
    elif (len2 == 0):
        for i in range(0, len1):
            output.append(arr1[i])
    else:
        arr1.append(sys.maxint)
        arr2.append(sys.maxint)

        for k in range(0, len1+len2):
            if (arr1[Ka] <= arr2[Kb]):
                output.append(arr1[Ka])
                Ka = Ka + 1
            else:
                output.append(arr2[Kb])
                Kb = Kb + 1
    return output

def merge_sort(arr, length):
    if length <= 1:
        return arr
    half = length/2

    array1 = merge_sort(arr[:half], len(arr[:half]))
    array2 = merge_sort(arr[half:], len(arr[half:]))
    sorted_array = merge_two_sorted_arrays(array1, array2)
    return sorted_array

size = 0
array = []

size = int(raw_input())
array = list(map(int, raw_input().split()))
sorted_array = merge_sort(array, size)

for i in range(0, len(sorted_array)):
    if (i < len(sorted_array) - 1):
        print(str(sorted_array[i]) + " ", end=''),
    else:
        print(str(sorted_array[i]) + " "),
