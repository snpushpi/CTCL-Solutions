def merge(l1,l2):
    i,j=0,0
    result = []
    while i<len(l1) or j<len(l2):
        if i<len(l1) and j<len(l2):
            if l1[i]<l2[j]:
                result.append(l1[i]) 
                i+=1
            else:
                result.append(l2[j])
                j+=1
        elif i==len(l1):
            result.append(l2[j])
            j+=1
        else:
            result.append(l1(i))
            i+=1
    return result
print(merge([1,2,5],[4,5,6]))