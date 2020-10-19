def three_pair_sum(l):
    n = len(l)
    elt_set = {l[i]:i for i in range(n)}
    
    res_set = []
    for i in range(n):
        for j in range(i+1,n):
            if -(l[i]+l[j]) in elt_set:
                val = -(l[i]+l[j]) 
                if elt_set[val]>j:
                    res_set.append([l[i],l[j],l[elt_set[val]]])
    return res_set
print(three_pair_sum([0,-1,2,-3,1]), three_pair_sum([1, -2, 1, 0, 5]))
    

