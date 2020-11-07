def main(arr):
    res = 0 
    for i in range(1,len(arr)):
        left = -float('inf')
        for j in range(i):
            left = max(left,arr[j])
        right = -float('inf')
        for j in range(i+1,n):
            right = max(right,arr[j])
        if arr[i]<min(left,right):
            res+= min(left,right)-arr[i]
    return res
print(main())        