import sys
def mid(a,b,c):
    if a <= b and a >= c:
        return a
    else:
        if b <= a and b>= c:
            return b
        else:
            return c
            
def quicksort(arr):
    left = []
    right = []
    midl = []
    if int(len(arr)) < 2:
        return(arr)
    else:
        m = len(arr)/2
        k = mid(arr[0], arr[m], arr[len(arr)-1])
        for i in range(0, len(arr)):
            if arr[i] < k:
                left.append(arr[i])
            else:
                if arr[i] > k:
                    right.append(arr[i])
                else:
                    midl.append(arr[i])
        return quicksort(left) + midl + quicksort(right)

array = sys.stdin.readline().split(' ')
for i in range(0, len(array)):
    array[i] = int(array[i])
array = quicksort(array)
print(array)
