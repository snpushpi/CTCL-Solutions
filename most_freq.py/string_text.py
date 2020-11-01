def only_once(arr,low,high):
    if len(arr)==3:
        if arr.count(arr[0])==1:
            return arr[0]
        else:
            return arr[-1]
    mid = (low+high)//2
    if not((arr[mid-1]==arr[mid]) or (arr[mid]==arr[mid+1])):
        return arr[mid]
    else:
        if arr[mid-1]==arr[mid] :
            if mid%2==1:
                return only_once(arr,mid+1,high)
            else:
                return only_once(arr,low,mid)
        else:
            if mid%2==1:
                return only_once(arr,low,mid-1)
            else:
                return only_once(arr,mid,high)
print(only_once([1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65],0,10))