def smaller(arr,j):
    left, right = j,j
    for i in range(j,-1,-1):
        if arr[i]>arr[j]:
            left = i-1
            break
    for i in range(j,len(arr)):
        if arr[i]>arr[j]:
            right = i-1
            break
    return left, right         
def count_subarrays(array):
    result_array = []
    for i in range(array):
        left, right = smaller(array,i)
        result_array.append(right-left+1)
    return result_array
print(count_subarrays([3,4,5]))