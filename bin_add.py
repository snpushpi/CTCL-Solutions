def pad(s1,l):
    s1 = s1[::-1]
    for i in range(l):
        s1+='0'
    return s1[::-1]
def bin_add(s1,s2):
    if len(s1)<len(s2):
        s1 = pad(s1,len(s2)-len(s1))
    else:
        s2 = pad(s2,len(s1)-len(s2))
    result = ''
    carry = 0
    for i in range(len(s1)-1,-1,-1):
        temp_res = (carry+int(s1[i])+int(s2[i]))%2
        carry = (carry+int(s1[i])+int(s2[i]))//2
        result+=str(temp_res)
    if carry==1:
        result+='1'
    return result[::-1]
print(bin_add('11','1'))