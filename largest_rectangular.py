def largest_rectangular(histogram):
    if len(histogram)==1:
        return histogram[0]
    if len(histogram)==2:
        return 2*min(histogram[0],histogram[1])
    n = len(histogram)
    mid = n//2
    f1 = histogram[:mid]
    f2 = histogram[mid:]
    f1_a,min_height1,min_hu1 = histogram[mid-1],histogram[mid-1],histogram[mid-1]
    for i in range(mid-1,-1,-1):
        if f1_a<min(min_height1,histogram[i])*(mid-1-i+1):
            f1_a = min(min_height1,histogram[i])*(mid-1-i+1)
            min_hu1 = min(min_height1,histogram[i])
        min_height1 = min(min_height1,histogram[i])
        
    f2_a,min_height2,min_hu2 = 0,histogram[mid],histogram[mid]
    for i in range(mid,n):
        if f2_a<min(min_height2,histogram[i])*(i-mid+1):
            f2_a = min(min_height2,histogram[i])*(i-mid+1)
            min_hu2 = min(min_height2,histogram[i])
        min_height2 = min(min_height2,histogram[i])

    if min_hu1<min_hu2:
        mid_best = min_hu1*(f1_a//min_hu1 + f2_a//min_hu2)
    else:
        mid_best = min_hu2*(f1_a//min_hu1 + f2_a//min_hu2)
    print(mid_best)
    return max(mid_best,largest_rectangular(f1),largest_rectangular(f2))
print(largest_rectangular([6, 2, 5, 4, 5, 1, 6]))

