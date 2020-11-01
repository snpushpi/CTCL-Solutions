def look_and_say(n):
    if n==1:
        return 1
    else:
        int_str = '1'
        
        for i in range(1,n):
            res_tuple = [[int_str[0],1]]
            for j in range(1,len(int_str)):
                if int_str[j]==int_str[j-1]:
                    res_tuple[-1][1]+=1
                else:
                    res_tuple.append([int_str[j],1])
            new_int_str = ''
            for elt in res_tuple:
                new_int_str+=str(elt[1])+str(elt[0])
            int_str = new_int_str
        return new_int_str
print(look_and_say(6))

    




