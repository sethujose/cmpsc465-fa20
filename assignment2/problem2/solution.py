from __future__ import print_function
import sys
import math

def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid] 
        R = arr[mid:] 
  
        mergeSort(L) 
        mergeSort(R) 
  
        i = j = k = 0
          
        while i < len(L) and j < len(R): 
            if L[i][2] < R[j][2]: 
                arr[k] = L[i] 
                i+= 1
            else: 
                arr[k] = R[j] 
                j+= 1
            k+= 1
          
        while i < len(L): 
            arr[k] = L[i] 
            i+= 1
            k+= 1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+= 1
            k+= 1

def getAngle(px, py, qx, qy):
    angleDeg = math.atan2(py - qy, px - qx) * 180 / math.pi
    return angleDeg

def getOrientation(Pa, Pb, P):
    Xa = Pa[0] - Pb[0]
    Ya = Pa[1] - Pb[1]
    Xb = P[0] - Pa[0]
    Yb = P[1] - Pa[1]
    return Xa*Yb - Xb*Ya

def graham_scan_core(array):
    stack = []

    if (len(array) < 3):
        return stack

    stack.append(array[0])
    stack.append(array[1])
    stack.append(array[2])

    for i in range(3, len(array)):
        P = array[i]
        while (stack):
            Pa = stack[-1]
            Pb = stack[-2]
            ori = getOrientation(Pa, Pb, P)

            if ori < 0:
                stack.pop()
            else:
                break
        stack.append(P)
    return stack

def graham_scan(array):
    min_y_coor = sys.float_info.max
    min_idx = sys.maxint

    for idx, item in enumerate(array):
        if (array[idx][1] < min_y_coor):
            min_y_coor = array[idx][1]
            min_idx = idx

    P0 = array.pop(min_idx)
    P0.append(0.0)

    for idx, item in enumerate(array):
        angle = getAngle(array[idx][0], array[idx][1], P0[0], P0[1])
        array[idx].append(angle)

    mergeSort(array)
    array.insert(0, P0)
    CH = graham_scan_core(array)
    return CH

num_lines = 0
array = []

num_lines = int(raw_input())
for i in range (num_lines):
    array.append(map(float, raw_input().split()))

#convert to y = ax - b form
for idx, item in enumerate(array):
    array[idx] = [array[idx][0], -array[idx][1]]

CH = graham_scan(array)

#find left most and rightmost points in CH
min_x_coor = sys.float_info.max
min_idx = sys.maxint
for idx, item in enumerate(CH):
    if (CH[idx][0] < min_x_coor):
        min_x_coor = CH[idx][0]
        min_idx = idx
left_point = CH.pop(min_idx)

max_x_coor = sys.float_info.min
max_idx = -sys.maxint - 1
for idx, item in enumerate(CH):
    if (CH[idx][0] > max_x_coor):
        max_x_coor = CH[idx][0]
        max_idx = idx
right_point = CH.pop(max_idx)

UE = []
LE = []
for item in CH:
    ori = getOrientation(right_point, left_point, item)
    if (ori > 0):
        LE.append(item)
    else:
        UE.append(item)

print(str(len(UE) + 2) + " " + str(len(LE) + 2), end='')