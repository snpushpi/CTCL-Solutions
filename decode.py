def decoding(s):
    result_string = ''
    rep_string = ''
    rep_num = ''
    flag = True
    temp_num = None
    if s.count('[')==1:
        for i in range(len(s)):
            if 48<=ord(s[i])<=57 and flag == True:
                rep_num+=s[i]
            elif s[i]=='[':
                flag = False
            elif s[i]!=']':
                if flag == False:
                    rep_string+=s[i]
                else:
                    result_string+=s[i]
        for j in range(int(rep_num)):
            result_string+=rep_string
        return result_string
  
    else:
        index = None
        rep_number = ''
        res_str = ''
        for i in range(len(s)):
            if s[i]=='[':
                index = i 
                break
            elif 48<=ord(s[i])<=57:
                rep_number+=s[i]
        rep_string = decoding(s[index+1:-1])
        for count in range(int(rep_number)):
            res_str+=rep_string
        return res_str
print(decoding("2[a2[b]]"))




