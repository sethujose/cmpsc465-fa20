import sys

def merge_two_sorted_arrays(arr1, arr2):
    output = []
    Ka = Kb = 1

    if ((arr1[0] == 0) and (arr2[0] == 0)):
        return output
    if (arr1[0] == 0):
        for i in range(1, len(arr2)):
            output.append(arr2[i])
    elif (arr2[0] == 0):
        for i in range(1, len(arr1)):
            output.append(arr1[i])
    else:
        arr1.append(sys.maxint)
        arr2.append(sys.maxint)

        for k in range(1, arr1[0] + arr2[0] + 1):
            if (arr1[Ka] <= arr2[Kb]):
                output.append(arr1[Ka])
                Ka = Ka + 1
            else:
                output.append(arr2[Kb])
                Kb = Kb + 1

    return output

array1 = []
array2 = []

array1 = list(map(int, raw_input().split()))
array2 = list(map(int, raw_input().split()))

sorted_array = merge_two_sorted_arrays(array1, array2)

print (len(sorted_array)),
for i in range(0, len(sorted_array)):
    print(sorted_array[i]),
