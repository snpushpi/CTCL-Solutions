def smallest_subarray(l,x):
    n = len(l)
    start = 0
    min_len = n
    for start in range(0,n):
        curr_sum = l[start]
        if curr_sum>x:
            return 1
        else:
            for j in range(start+1,n):
                curr_sum+=l[j]
                if curr_sum>x:
                    min_len=min(min_len,j-start+1)
    return min_len
                    
print(smallest_subarray([1, 4, 45, 6, 0, 19],51))
