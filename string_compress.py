def string_compression(string1):
    start = string1[0]
    count= 1
    res_str = ''
    for i in range(1,len(string1)):
        if string1[i]==start:
            count+=1
            if i == len(string1)-1:
                res_str = res_str + start + str(count)
        else:
            res_str = res_str + start+ str(count)
            count = 1
            start = string1[i]
            if i == len(string1)-1:
                res_str = res_str + start + str(count)
    if len(res_str)< len(string1):
        return res_str 
    else:
        return string1
print(string_compression('aabcccccaaab'))
