def counter(s):
    result = {}
    for c in s:
        if c in result:
            result[c]+=1
        else:
            result[c]=1
    return result
def permutation(s,t):
    return counter(s)==counter(t)
print(permutation('aca','abc'))