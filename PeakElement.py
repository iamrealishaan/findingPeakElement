# finding peak element in the array
def FindPeak(arr,n):
    if(n==1):
        return 0
    if (arr[0]>=arr[1]):
        return 0
    if (arr[n-1]>=arr[n-2]):
        return n-1
    for i in range(1, n-1):
        if(arr[i]>=arr[i-1] and arr[i]>=arr[i+1]) :
            return i
    # if no peak element found
    return -1
arr = [1,7,23,45,3,0,90]
n = len(arr)
print("Index of a peak point is", FindPeak(arr,n))

