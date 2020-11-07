def main(arr,k):
    if len(arr)<k:
        return sum(arr)
    if k==1:
        return max(arr[0],arr[-1])
    return max(arr[0]+main(arr[1:],k-1),arr[-1]+main(arr[:-1],k-1))
print(main([-2,-1,9,0,-3,-4,4],4))