import sys
k = 11

def insertion_sort(arr):
    for i in range(0, len(arr)):
        j = i - 1
        while (j >= 0) and (arr[j] > arr[j+1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
    return arr

def merge (larr, rarr):
    left = 0
    right = 0
    full = [0 for i in range (len(larr) + len(rarr))]
    while (len(larr) > left) and (len(rarr) > right):
        if larr[left] < rarr[right]:
            full[right + left] = larr[left]
            left += 1
        else:
            full[right + left] = rarr[right]
            right += 1
    while left < len(larr):
        full[left + right] = larr[left]
        left += 1
    while right < len(rarr):
        full[left + right] = rarr[right]
        right += 1
    return full

def full_sort (arr):
    if len(arr) >= k:
        arr = merge(full_sort(arr[0:int(len(arr)/2)]), full_sort(arr[int(len(arr)/2):len(arr)+1]))
    else:
        arr = insertion_sort(arr)
    return arr

arr = sys.stdin.readline().split(' ')
for i in range(0,len(arr)):
    arr[i] = int(arr[i])
arr = full_sort(arr)
print (arr)
