def main(arr,m):
    arr.sort()
    n = len(arr)
    min_dif = float('inf')
    for i in range(n-m):
        min_dif = min(min_dif,arr[i+m-1]-arr[i])
