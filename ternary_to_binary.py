def distinct_pair_k(l,k):
    count=0
    
    for i in range(len(l)):
        count+=(l.count(l[i]-k)+l.count(l[i]+k))
    return count/2
print(distinct_pair_k([4,4,4,3,3,3],1))
